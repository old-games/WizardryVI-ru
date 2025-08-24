import PIL.Image

import tools.ega


PALETTE = tools.ega.PALETTE

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
