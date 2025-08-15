import PIL.Image


PALETTE = list((([
    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0xff, 0xff, 0xff, 0xff), # 1: White
    (0x4e, 0x4b, 0xf7, 0xff), # 2: Blue
    (0xf0, 0x59, 0xf9, 0xff), # 3: Purple
    (0xef, 0x59, 0x50, 0xff), # 4: Rose
    (0xfe, 0xff, 0x62, 0xff), # 5: Yellow
    (0x70, 0xfb, 0x5e, 0xff), # 6: Lime
    (0x73, 0xfb, 0xfd, 0xff), # 7: Aqua
    (0x4b, 0x4b, 0x4b, 0xff), # 8: Gray
    (0xa0, 0xa0, 0xa0, 0xff), # 9: Silver
    (0x0e, 0x03, 0x9b, 0xff), # 10: Navy
    (0x96, 0x1e, 0x9b, 0xff), # 11: Violet
    (0x96, 0x1e, 0x11, 0xff), # 12: Red
    (0x98, 0x50, 0x19, 0xff), # 13: Brown
    (0x38, 0x9d, 0x26, 0xff), # 14: Green
    (0x00, 0x00, 0x00, 0x00), # 15: Transparent
])))


def _parse_entries(uncompressed_bytes: bytes) -> list[tuple[bytes, bytes]]:
    offsets = []
    i = 0
    min_offset = None
    while True:
        if i + 24 > len(uncompressed_bytes):
            raise ValueError(f'Partial entry encountered at position {i}')
        offset = int.from_bytes(uncompressed_bytes[i:i+2], 'little')
        entry_header = uncompressed_bytes[i:i+24]
        if any(entry_header):
            offsets.append((offset, i, entry_header))
            if min_offset is None or offset < min_offset:
                min_offset = offset
        i += 24
        if i == min_offset:
            break
    if not offsets:
        return []
    offsets_sorted = sorted(offsets, key=lambda x: x[0])
    offsets_only = [o[0] for o in offsets_sorted]
    offsets_only.append(len(uncompressed_bytes))
    entries = []
    for idx in range(len(offsets_only) - 1):
        entry_header = offsets_sorted[idx][2]
        data_start = offsets_only[idx]
        data_end = offsets_only[idx + 1]
        entry_data = uncompressed_bytes[data_start:data_end]
        entries.append((entry_header, entry_data))
    return entries


def _entry_to_image(entry_header, data):
    width_blocks = entry_header[2]
    height_blocks = entry_header[3]
    width = width_blocks * 8
    height = height_blocks * 8
    bitmask = entry_header[4:24]
    blocks = []
    data_idx = 0
    for block_idx in range(width_blocks * height_blocks):
        byte_idx = block_idx // 8
        bit_idx = block_idx % 8
        if byte_idx < len(bitmask) and (bitmask[byte_idx] & (1 << bit_idx)):
            block_bytes = data[data_idx:data_idx+32]
            data_idx += 32
        else:
            block_bytes = bytes([255]*32)
        blocks.append(block_bytes)
    img = [[[255, 255, 255, 0] for _ in range(width)] for _ in range(height)]
    for block_num, block in enumerate(blocks):
        bx = block_num % width_blocks
        by = block_num // width_blocks
        if len(block) < 32:
            block = block + bytes([255] * (32 - len(block)))
        for y in range(8):
            for x in range(8):
                color = 0
                for bit in range(4):
                    plane_byte = block[bit * 8 + y]
                    color |= ((plane_byte >> (7 - x)) & 1) << bit
                img[by*8 + y][bx*8 + x] = PALETTE[color]
    from PIL import Image
    flat_img = b''.join(bytes(px) for row in img for px in row)
    pil_img = Image.frombytes('RGBA', (width, height), flat_img)
    return pil_img


def decode(data: bytes) -> list[PIL.Image.Image]:
    entries = _parse_entries(data)
    images = []
    for entry_header, entry_data in entries:
        img = _entry_to_image(entry_header, entry_data)
        images.append(img)
    return images
