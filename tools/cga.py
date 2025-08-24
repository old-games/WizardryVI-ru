import PIL.Image


PALETTE = [
    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0x74, 0xfb, 0xfd, 0xff), # 1: Cyan
    (0xf0, 0x59, 0xf9, 0xff), # 2: Magenta
    (0xff, 0xff, 0xff, 0xff), # 3: White
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
