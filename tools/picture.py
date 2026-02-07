import PIL.Image
import warnings


def _rgba_distance_sq(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> int:
    # Ignore alpha distance when both are fully opaque; otherwise include it.
    dr = a[0] - b[0]
    dg = a[1] - b[1]
    db = a[2] - b[2]
    da = a[3] - b[3]
    return dr * dr + dg * dg + db * db + da * da


def _nearest_palette_index(rgba: tuple[int, int, int, int]) -> tuple[int, bool]:
    """Return (palette_index, exact_match)."""
    # Fast path for exact colors.
    try:
        return _ALPHA_PALETTE_INDEX[rgba], True
    except KeyError:
        pass
    # If pixel is fully transparent, always map to transparent.
    if rgba[3] == 0:
        return 15, False
    best_i = 0
    best_d = None
    for i, p in enumerate(ALPHA_PALETTE):
        d = _rgba_distance_sq(rgba, p)
        if best_d is None or d < best_d:
            best_d = d
            best_i = i
    return best_i, False


ALPHA_PALETTE = [
    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0xff, 0xff, 0xff, 0xff), # 1: White
    (0x4e, 0x4b, 0xf7, 0xff), # 2: Blue
    (0xf0, 0x59, 0xf9, 0xff), # 3: Purple
    (0xef, 0x59, 0x50, 0xff), # 4: Rose
    (0xfe, 0xff, 0x62, 0xff), # 5: Yellow
    (0x70, 0xfb, 0x5e, 0xff), # 6: Lime
    (0x74, 0xfb, 0xfd, 0xff), # 7: Aqua
    (0x4b, 0x4b, 0x4b, 0xff), # 8: Gray
    (0xa0, 0xa0, 0xa0, 0xff), # 9: Silver
    (0x0e, 0x01, 0x9b, 0xff), # 10: Navy
    (0x96, 0x1e, 0x9b, 0xff), # 11: Violet
    (0x96, 0x1e, 0x11, 0xff), # 12: Red
    (0x98, 0x50, 0x19, 0xff), # 13: Brown
    (0x38, 0x9d, 0x26, 0xff), # 14: Green
    (0x00, 0x00, 0x00, 0x00), # 15: Transparent
]


_ALPHA_PALETTE_INDEX: dict[tuple[int, int, int, int], int] = {p: i for i, p in enumerate(ALPHA_PALETTE)}


def _parse_entries(uncompressed_bytes: bytes) -> list[tuple[bytes, bytes]]:
    offsets = []
    i = 0
    min_offset = None
    while True:
        if i + 24 > len(uncompressed_bytes):
            raise ValueError(f'Partial entry encountered at position {i}.')
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
    assert len(uncompressed_bytes) == data_end, 'Extra data at end of PIC stream.'
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
    assert len(data) >= data_idx
    # assert len(data) == data_idx, f'Extra data at end of entry: {data[data_idx:].hex().upper()}.'
    img = [[[255, 255, 255, 0] for _ in range(width)] for _ in range(height)]
    for block_num, block in enumerate(blocks):
        bx = block_num % width_blocks
        by = block_num // width_blocks
        assert len(block) == 32, 'Unexpected short block.'
        for y in range(8):
            for x in range(8):
                color = 0
                for bit in range(4):
                    plane_byte = block[bit * 8 + y]
                    color |= ((plane_byte >> (7 - x)) & 1) << bit
                img[by*8 + y][bx*8 + x] = ALPHA_PALETTE[color]
    flat_img = b''.join(bytes(px) for row in img for px in row)
    pil_img = PIL.Image.frombytes('RGBA', (width, height), flat_img)
    return pil_img


def decode(data: bytes) -> list[PIL.Image.Image]:
    entries = _parse_entries(data)
    images = []
    for entry_header, entry_data in entries:
        img = _entry_to_image(entry_header, entry_data)
        images.append(img)
    return images


def _image_to_blocks(img: PIL.Image.Image, *, warn_on_non_palette: bool = True, warn_limit: int = 10) -> tuple[int, int, bytes, list[bytes]]:
    '''Convert RGBA image to `.PIC` blocks.

    Returns (width_blocks, height_blocks, bitmask20, blocks32).

    The decoder (`_entry_to_image`) iterates blocks in strict block order and, when a bitmask
    bit is set, consumes 32 bytes from the data stream.

    Therefore, for a correct sparse encoding we must:
    - set the bitmask bit only for blocks that are present in the stream
    - write 32 bytes for each present block, in increasing block index order
    Fully transparent blocks should be omitted (bitmask bit 0), and the decoder will treat
    them as transparent (0xFF*32).
    '''

    img = img.convert('RGBA')
    width, height = img.size
    if width % 8 or height % 8:
        raise ValueError(f'PIC images must have width/height multiples of 8, got {width}x{height}.')
    width_blocks = width // 8
    height_blocks = height // 8
    if width_blocks * height_blocks > 160:
        raise ValueError(f'PIC supports at most 160 blocks (bitmask is 20 bytes) but got {width_blocks*height_blocks}.')

    pix = list(img.getdata())
    non_exact_counter: dict[tuple[int, int, int, int], int] = {}
    indices: list[int] = []
    for rgba in pix:
        idx, exact = _nearest_palette_index(rgba)
        if not exact:
            non_exact_counter[rgba] = non_exact_counter.get(rgba, 0) + 1
        indices.append(idx)

    if non_exact_counter:
        if warn_on_non_palette:
            # Report top offenders.
            total = sum(non_exact_counter.values())
            top = sorted(non_exact_counter.items(), key=lambda kv: kv[1], reverse=True)[:warn_limit]
            samples = ', '.join([f'{c}x{rgba}' for rgba, c in top])
            warnings.warn(
                f'Non-palette colors encountered in PIC encode: {len(non_exact_counter)} unique, {total} pixels. '
                f'Mapped to nearest ALPHA_PALETTE. Top: {samples}',
                RuntimeWarning,
                stacklevel=2,
            )
        else:
            raise ValueError(f'Non-palette colors encountered in PIC encode: {len(non_exact_counter)} unique colors.')

    def get_idx(x: int, y: int) -> int:
        return indices[y * width + x]

    total_blocks = width_blocks * height_blocks
    bitmask = bytearray(20)
    blocks: list[bytes] = []
    for block_idx in range(total_blocks):
        bx = block_idx % width_blocks
        by = block_idx // width_blocks
        x0 = bx * 8
        y0 = by * 8

        # Determine if block has any non-transparent pixels.
        has_data = False
        for yy in range(8):
            for xx in range(8):
                if get_idx(x0 + xx, y0 + yy) != 15:
                    has_data = True
                    break
            if has_data:
                break
        if not has_data:
            continue

        # Mark this block as present.
        byte_idx = block_idx // 8
        bit_idx = block_idx % 8
        bitmask[byte_idx] |= 1 << bit_idx

        # Build 4 planar bitplanes, 8 bytes per plane.
        plane_bytes = bytearray(32)
        for row in range(8):
            for plane in range(4):
                b = 0
                for col in range(8):
                    pal = get_idx(x0 + col, y0 + row)
                    bit = (pal >> plane) & 1
                    b |= bit << (7 - col)
                plane_bytes[plane * 8 + row] = b
        blocks.append(bytes(plane_bytes))

    return width_blocks, height_blocks, bytes(bitmask), blocks


def encode(images: list[PIL.Image.Image], *, warn_on_non_palette: bool = True) -> bytes:
    '''Encode a list of PIL images to uncompressed `.PIC` bytes.

    Notes/constraints inferred from decode():
    - Each entry header is 24 bytes.
    - Header[0:2] is a little-endian offset to the entry data.
    - Header[2] width in 8x8 blocks, Header[3] height in blocks.
    - Header[4:24] is a 20-byte bitmask (max 160 blocks). If bit is 1, a 32-byte block
      exists in the entry data; otherwise it is implicitly transparent.
    - Block format is 4 bitplanes (4 * 8 bytes). Pixel index is composed from plane bits.

    This encoder will quantize any non-palette RGBA colors to the nearest entry in
    `ALPHA_PALETTE` and emit a `RuntimeWarning` unless `warn_on_non_palette=False`.
    '''

    if not images:
        return b''

    # Encode each image to blocks and bitmask first.
    entries: list[tuple[bytes, bytes]] = []
    for img in images:
        wb, hb, bitmask, blocks = _image_to_blocks(img, warn_on_non_palette=warn_on_non_palette)
        header = bytearray(24)
        # Offset is filled later.
        header[2] = wb & 0xff
        header[3] = hb & 0xff
        header[4:24] = bitmask
        data = b''.join(blocks)
        entries.append((bytes(header), data))

    # Original assets use a fixed 600-byte header table (25 * 24 records).
    # Some records are all-zero and are ignored by `_parse_entries`.
    # Data offsets stored in header[0:2] are **byte offsets** into the decompressed stream.
    HEADER_SLOTS = 25
    HEADER_SIZE = 24
    header_table_size = HEADER_SLOTS * HEADER_SIZE

    if len(entries) > HEADER_SLOTS:
        raise ValueError(f'PIC supports at most {HEADER_SLOTS} entries but got {len(entries)}.')

    out_headers = bytearray(b'\x00' * header_table_size)
    out_data = bytearray()
    current_offset = header_table_size
    for idx, (hdr, data) in enumerate(entries):
        hdr = bytearray(hdr)
        hdr[0:2] = int(current_offset).to_bytes(2, 'little')
        out_headers[idx * HEADER_SIZE: (idx + 1) * HEADER_SIZE] = hdr
        out_data.extend(data)
        current_offset += len(data)

    return bytes(out_headers + out_data)
