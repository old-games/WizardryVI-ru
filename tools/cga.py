import PIL.Image

import tools.picture


PALETTE = [
    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0x74, 0xfb, 0xfd, 0xff), # 1: Cyan
    (0xf0, 0x59, 0xf9, 0xff), # 2: Magenta
    (0xff, 0xff, 0xff, 0xff), # 3: White
]

ONE_BIT_PALETTE = [
    tools.picture.ALPHA_PALETTE[-1], # 1: Transparent
    tools.picture.ALPHA_PALETTE[0],  # 0: Black
]


def decode(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert len(data) & 1 == 0
    assert len(data) >= width*height//4
    flat_img = bytearray()
    if width & 3:
        width += 4 - width & 3
    even, odd = iter(data[:len(data)//2]), iter(data[len(data)//2:])
    for _ in range(height):
        for _ in range(0, width, 4):
            w = next(even)
            flat_img.extend(PALETTE[w >> 6][:3])
            flat_img.extend(PALETTE[(w >> 4) & 3][:3])
            flat_img.extend(PALETTE[(w >> 2) & 3][:3])
            flat_img.extend(PALETTE[w & 3][:3])
        odd, even = even, odd
    pil_img = PIL.Image.frombytes('RGB', (width, height), flat_img)
    return pil_img


def decode_without_interleaving(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert len(data) & 1 == 0
    assert len(data) >= width*height//4
    flat_img = bytearray()
    if width & 3:
        width += 4 - width & 3
    even = iter(data)
    for _ in range(height):
        for _ in range(0, width, 4):
            w = next(even)
            flat_img.extend(PALETTE[w >> 6][:3])
            flat_img.extend(PALETTE[(w >> 4) & 3][:3])
            flat_img.extend(PALETTE[(w >> 2) & 3][:3])
            flat_img.extend(PALETTE[w & 3][:3])
    pil_img = PIL.Image.frombytes('RGB', (width, height), flat_img)
    return pil_img


def decode_one_bit(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert len(data) & 1 == 0
    assert len(data) >= width*height//4
    flat_img = bytearray()
    if width & 3:
        width += 4 - width & 3
    even = iter(data)
    for _ in range(height):
        for _ in range(0, width, 4):
            w = next(even)
            assert w >> 6 in (0, 3)
            assert (w >> 4) & 3 in (0, 3)
            assert (w >> 2) & 3 in (0, 3)
            assert w & 3 in (0, 3)
            flat_img.extend(ONE_BIT_PALETTE[w >> 7])
            flat_img.extend(ONE_BIT_PALETTE[(w >> 4) & 1])
            flat_img.extend(ONE_BIT_PALETTE[(w >> 2) & 1])
            flat_img.extend(ONE_BIT_PALETTE[w & 1])
    pil_img = PIL.Image.frombytes('RGBA', (width, height), flat_img)
    return pil_img


def encode(img: PIL.Image.Image, pad_size: int = 0) -> bytes:
    '''
    Encode a PIL.Image.Image (mode 'RGB', width multiple of 4) to CGA bytes with interleaving.
    Each byte encodes 4 pixels: bits 6-7, 4-5, 2-3, 0-1.
    Uses PALETTE (first 4 colors).
    '''
    width, height = img.size
    assert width % 4 == 0, 'Width must be a multiple of 4.'
    img = img.convert('RGB')
    data = img.tobytes()
    palette_map = {tuple(PALETTE[i][:3]): i for i in range(4)}
    even_bytes = bytearray()
    odd_bytes = bytearray()
    for y in range(height):
        row_bytes = bytearray()
        for x in range(0, width, 4):
            idxs = [(y * width + x + i) * 3 for i in range(4)]
            rgbs = [tuple(data[idx:idx+3]) for idx in idxs]
            vals = [palette_map.get(rgb, 0) & 3 for rgb in rgbs]
            b = (vals[0] << 6) | (vals[1] << 4) | (vals[2] << 2) | vals[3]
            row_bytes.append(b)
        # Interleave rows: even and odd
        if y % 2 == 0:
            even_bytes.extend(row_bytes)
        else:
            odd_bytes.extend(row_bytes)
    if pad_size:
        for pad in (even_bytes, odd_bytes):
            pad_len = (-len(pad)) % pad_size
            if pad_len:
                pad.extend(b'\x00' * pad_len)
    return bytes(even_bytes + odd_bytes)


def encode_without_interleaving(img: PIL.Image.Image) -> bytes:
    '''
    Encode a PIL.Image.Image (mode 'RGB', width multiple of 4) to CGA bytes without interleaving.
    Each byte encodes 4 pixels: bits 6-7, 4-5, 2-3, 0-1.
    Uses PALETTE (first 4 colors).
    '''
    width, height = img.size
    assert width % 4 == 0, 'Width must be a multiple of 4.'
    img = img.convert('RGB')
    data = img.tobytes()
    palette_map = {tuple(PALETTE[i][:3]): i for i in range(4)}
    encoded = bytearray()
    for y in range(height):
        for x in range(0, width, 4):
            idxs = [(y * width + x + i) * 3 for i in range(4)]
            rgbs = [tuple(data[idx:idx+3]) for idx in idxs]
            vals = [palette_map.get(rgb, 0) & 3 for rgb in rgbs]
            b = (vals[0] << 6) | (vals[1] << 4) | (vals[2] << 2) | vals[3]
            encoded.append(b)
    return bytes(encoded)


def encode_one_bit(img: PIL.Image.Image) -> bytes:
    '''
    Encode a PIL.Image.Image (mode 'RGBA', width multiple of 4) to CGA one-bit bytes.
    Each byte encodes 4 pixels: bits 6-7, 4-5, 2-3, 0-1.
    Uses ONE_BIT_PALETTE (transparent/black).
    '''
    width, height = img.size
    assert width % 4 == 0, 'Width must be a multiple of 4.'
    img = img.convert('RGBA')
    data = img.tobytes()
    # Map: transparent -> 0, black -> 3.
    palette_map = {tuple(ONE_BIT_PALETTE[0]): 0, tuple(ONE_BIT_PALETTE[1]): 3}
    encoded = bytearray()
    for y in range(height):
        for x in range(0, width, 4):
            idxs = [(y * width + x + i) * 4 for i in range(4)]
            vals = []
            for idx in idxs:
                rgba = tuple(data[idx:idx+4])
                val = palette_map.get(rgba, 0) & 3
                vals.append(val)
            b = (vals[0] << 6) | (vals[1] << 4) | (vals[2] << 2) | vals[3]
            encoded.append(b)
    return bytes(encoded)
