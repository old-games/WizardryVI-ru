import PIL.Image


def encode(image: PIL.Image.Image) -> PIL.Image.Image:
    return image.resize((image.width * 10, image.height * 10), resample=0)


def decode(image: PIL.Image.Image) -> PIL.Image.Image:
    assert image.width % 10 == 0 and image.height % 10 == 0, 'Image dimensions must be multiples of 10.'
    return image.resize((image.width // 10, image.height // 10), resample=0)
