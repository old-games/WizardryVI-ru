import PIL.Image
from PIL import ImageEnhance, ImageFilter

import tools.cga
import tools.ega


for palette_name, palette in (('cga', tools.cga.PALETTE), ('ega', tools.ega.PALETTE)):
    flat_palette = []
    for color in palette:
        flat_palette.extend(color[:3])

    palette_img = PIL.Image.new('P', (1, 1))
    palette_img.putpalette(flat_palette)

    img = PIL.Image.open('tools/vnd.png').convert('RGB')
    # Apply sharpen
    img = img.filter(ImageFilter.SHARPEN)
    # Apply contrast
    img = ImageEnhance.Contrast(img).enhance(1.5)
    # Apply saturation
    img = ImageEnhance.Color(img).enhance(1.5)

    img = img.quantize(palette=palette_img, dither=PIL.Image.FLOYDSTEINBERG)
    img.resize((img.size[0]*10, img.size[1]*10)).save(f'tools/vnd-{palette_name}.png')
