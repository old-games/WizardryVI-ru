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
