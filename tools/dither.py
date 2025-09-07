import PIL.Image
from PIL import ImageEnhance, ImageFilter

import tools.cga
import tools.ega
import tools.tandy

img = PIL.Image.open('tools/vnd.png').convert('RGB')
# Apply sharpen
img = img.filter(ImageFilter.SHARPEN)
# Apply contrast
img = ImageEnhance.Contrast(img).enhance(1.5)
# Apply saturation
img = ImageEnhance.Color(img).enhance(1.5)

for palette_name, palette, encode_func, ext, decode_func in [
    ('cga', tools.cga.PALETTE, tools.cga.encode, 'cga', tools.cga.decode),
    ('ega', tools.ega.PALETTE, tools.ega.encode, 'ega', tools.ega.decode),
    ('tandy', tools.tandy.PALETTE, tools.tandy.encode, 't16', tools.tandy.decode),
]:
    flat_palette = []
    for color in palette:
        flat_palette.extend(color[:3])

    palette_img = PIL.Image.new('P', (1, 1))
    palette_img.putpalette(flat_palette)

    dithered = img.quantize(palette=palette_img, dither=PIL.Image.FLOYDSTEINBERG)
    dithered.resize((dithered.size[0]*10, dithered.size[1]*10)).save(f'tools/vnd-{palette_name}.png')

    # Save encoded binary format
    encoded = encode_func(dithered)
    with open(f'tools/vnd-{palette_name}.{ext}', 'wb') as f:
        f.write(encoded)

    # Decode and check
    decoded = decode_func(encoded, dithered.size[0], dithered.size[1])
    # Convert dithered to RGB for fair comparison
    dithered_rgb = dithered.convert('RGB')
    if list(dithered_rgb.getdata()) != list(decoded.getdata()):
        print(f"Warning: {palette_name} decode does not match dithered image.")
