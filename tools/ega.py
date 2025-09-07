import PIL.Image

import tools.picture


PALETTE = [
    *tools.picture.ALPHA_PALETTE[:-1],
    (0x39, 0x9d, 0xa0, 0xff), # 15: Teal
]

ONE_BIT_PALETTE = [
    tools.picture.ALPHA_PALETTE[-1], # 1: Transparent
    tools.picture.ALPHA_PALETTE[0],  # 0: Black
]

MAD_DOG_COSMIC_FORGE_PALETTE = [
    PALETTE[0], # 0: Black
    (0xfc, 0xfc, 0xfc, 0xff), # 1: White
    (0x4d, 0x4a, 0xf3, 0xff), # 2: Blue
    (0xed, 0x57, 0xf5, 0xff), # 3: Purple
    (0xec, 0x57, 0x4e, 0xff), # 4: Rose
    (0xfb, 0xfb, 0x61, 0xff), # 5: Yellow
    (0x6f, 0xf7, 0x5d, 0xff), # 6: Lime
    (0x72, 0xf7, 0xfa, 0xff), # 7: Aqua
    (0x4a, 0x4a, 0x4a, 0xff), # 8: Gray
    (0x9e, 0x9e, 0x9e, 0xff), # 9: Silver
    (0x0d, 0x01, 0x98, 0xff), # 10: Navy
    (0x94, 0x1e, 0x99, 0xff), # 11: Violet
    (0x93, 0x1d, 0x10, 0xff), # 12: Red
    (0x96, 0x4f, 0x18, 0xff), # 13: Brown
    (0x36, 0x9b, 0x25, 0xff), # 14: Green
    (0x38, 0x9b, 0x9d, 0xff), # 15: Teal
]


def _byte_to_bits(x: int) -> list[int]:
    result = []
    for i in range(8):
        result.append(int(bool(x & (1 << i))))
    return result


def _bits_to_int(bits: list[int]) -> int:
    result = 0
    for i, x in enumerate(bits):
        if x:
            result |= 1 << i
    return result


def decode(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert len(data) & 3 == 0
    assert len(data) >= width*height//2
    planes = [data[:len(data)//4], data[len(data)//4:len(data)//4*2], data[len(data)//4*2:len(data)//4*3], data[len(data)//4*3:]]
    flat_img = bytearray()
    its = list(map(iter, planes))
    if width & 7:
        width += 8 - width & 7
    for _ in range(height):
        for _ in range(0, width, 8):
            ww = list(map(_byte_to_bits, map(next, its)))
            for i in reversed(range(8)):
                flat_img.extend(PALETTE[_bits_to_int([ww[0][i], ww[1][i], ww[2][i], ww[3][i]])][:3])
    pil_img = PIL.Image.frombytes('RGB', (width, height), flat_img)
    return pil_img


def decode_one_bit(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert len(data) >= width*height//8, f'Not enough data: {len(data)} for {width}x{height}.'
    flat_img = bytearray()
    its = iter(data)
    for _ in range(height):
        for _ in range(0, width, 8):
            w = next(its)
            bits = _byte_to_bits(w)
            for b in reversed(bits):
                flat_img.extend(ONE_BIT_PALETTE[b])
    pil_img = PIL.Image.frombytes('RGBA', (width, height), flat_img)
    return pil_img


def encode(img: PIL.Image.Image, pad_size: int = 0) -> bytes:
    width, height = img.size
    assert width % 8 == 0, 'Width must be a multiple of 8.'
    img = img.convert('RGB')
    data = img.tobytes()
    planes = [bytearray() for _ in range(4)]
    palette_map = {tuple(PALETTE[i][:3]): i for i in range(16)}
    for y in range(height):
        for x in range(0, width, 8):
            bits = [[0]*8 for _ in range(4)]
            for i in range(8):
                idx = (y * width + x + i) * 3
                rgb = tuple(data[idx:idx+3])
                pal_idx = palette_map.get(rgb, 0)
                for p in range(4):
                    bits[p][i] = (pal_idx >> p) & 1
            for p in range(4):
                b = 0
                # Reverse order: leftmost pixel is bit 7
                for i in range(8):
                    b |= bits[p][i] << (7 - i)
                planes[p].append(b)
    if pad_size:
        for p in range(4):
            pad_len = (-len(planes[p])) % pad_size
            if pad_len:
                planes[p].extend([0] * pad_len)
    return b''.join(planes)

def encode_one_bit(img: PIL.Image.Image) -> bytes:
    width, height = img.size
    assert width % 8 == 0, 'Width must be a multiple of 8.'
    img = img.convert('RGBA')
    data = img.tobytes()
    palette_map = {
        tuple(ONE_BIT_PALETTE[0]): 0, # Black
        tuple(ONE_BIT_PALETTE[1]): 1, # Transparent
    }
    result = bytearray()
    for y in range(height):
        for x in range(0, width, 8):
            b = 0
            for i in range(8):
                idx = (y * width + x + i) * 4
                rgba = tuple(data[idx:idx+4])
                bit = palette_map.get(rgba, 0)
                b |= (bit << (7 - i))
            result.append(b)
    return bytes(result)
