import PIL.Image

import tools.ega
import tools.picture


PALETTE = tools.ega.PALETTE
ONE_BIT_PALETTE = [
    tools.picture.ALPHA_PALETTE[-1], # 1: Transparent
    tools.picture.ALPHA_PALETTE[0],  # 0: Black
]

def decode(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert width & 1 == 0
    assert len(data) >= width*height//2
    flat_img = bytearray()
    it = iter(data)
    for _ in range(0, height):
        for _ in range(0, width, 2):
            w = next(it)
            flat_img.extend(PALETTE[w >> 4][:3])
            flat_img.extend(PALETTE[w & 0x0f][:3])
    pil_img = PIL.Image.frombytes('RGB', (width, height), flat_img)
    return pil_img

def decode_one_bit(data: bytes, width: int, height: int) -> PIL.Image.Image:
    assert width & 1 == 0
    assert len(data) >= width*height//2
    flat_img = bytearray()
    it = iter(data)
    for _ in range(0, height):
        for _ in range(0, width, 2):
            w = next(it)
            assert w >> 4 in (0, 0x0f)
            assert w & 0x0f in (0, 0x0f)
            flat_img.extend(ONE_BIT_PALETTE[(w >> 4) & 1])
            flat_img.extend(ONE_BIT_PALETTE[w & 1])
    pil_img = PIL.Image.frombytes('RGBA', (width, height), flat_img)
    return pil_img

def encode(img: PIL.Image.Image) -> bytes:
    """
    Encode a PIL.Image.Image (mode 'RGB', width even) to Tandy packed bytes.
    Each byte encodes two pixels: high nibble is left pixel, low nibble is right pixel.
    Uses PALETTE (first 16 colors).
    """
    width, height = img.size
    assert width % 2 == 0, "Width must be even"
    img = img.convert('RGB')
    data = img.tobytes()
    palette_map = {tuple(PALETTE[i][:3]): i for i in range(16)}
    encoded = bytearray()
    for y in range(height):
        for x in range(0, width, 2):
            idx1 = (y * width + x) * 3
            idx2 = (y * width + x + 1) * 3
            rgb1 = tuple(data[idx1:idx1+3])
            rgb2 = tuple(data[idx2:idx2+3])
            nibble1 = palette_map.get(rgb1, 0)
            nibble2 = palette_map.get(rgb2, 0)
            encoded.append((nibble1 << 4) | (nibble2 & 0x0F))
    # Pad to 1024 bytes with zeros
    pad_len = (-len(encoded)) % 1024
    if pad_len:
        encoded.extend(b'\x00' * pad_len)
    return bytes(encoded)
