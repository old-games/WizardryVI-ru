import PIL.Image


def merge(images: list[PIL.Image.Image]) -> PIL.Image.Image:
    assert len(images) == 9
    w, h = images[0].size
    merged = PIL.Image.new("RGBA", (w * 3, h * 3))
    for idx, img in enumerate(images):
        x = (idx % 3) * w
        y = (idx // 3) * h
        merged.paste(img, (x, y))
    return merged
