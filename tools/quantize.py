import PIL.Image

import tools.cga
import tools.ega


# This conversion only works on `TITLEPAG`.
# For `GRAVEYRD` and `DRAGONSC` colors do not code consistently.
_EGA_TO_CGA = (
    0, # Black  -> Black
    3, # White  -> White
    1, # Blue   -> Cyan
    2, # Purple -> Magenta
    2, # Rose   -> Magenta
    3, # Yellow -> White
    1, # Lime   -> Cyan
    1, # Aqua   -> Cyan
    2, # Gray   -> Magenta
    1, # Silver -> Cyan
    2, # Navy   -> Magenta
    2, # Violet -> Magenta
    2, # Red    -> Magenta
    2, # Brown  -> Magenta
    1, # Green  -> Cyan
    1, # Teal   -> Cyan
)
_EGA_TO_CGA_ONE_BIT = (0, 1)

"""
    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0xff, 0xff, 0xff, 0xff), # 1: White
    (0x4e, 0x4b, 0xf7, 0xff), # 2: Blue
    (0xf0, 0x59, 0xf9, 0xff), # 3: Purple
    (0xef, 0x59, 0x50, 0xff), # 4: Rose
    (0xfe, 0xff, 0x62, 0xff), # 5: Yellow
    (0x70, 0xfb, 0x5e, 0xff), # 6: Lime
    (0x74, 0xfb, 0xfd, 0xff), # 7: Aqua
    (0x4b, 0x4b, 0x4b, 0xff), # 8: Gray
    (0xa0, 0xa0, 0xa0, 0xff), # 9: Silver
    (0x0e, 0x01, 0x9b, 0xff), # 10: Navy
    (0x96, 0x1e, 0x9b, 0xff), # 11: Violet
    (0x96, 0x1e, 0x11, 0xff), # 12: Red
    (0x98, 0x50, 0x19, 0xff), # 13: Brown
    (0x38, 0x9d, 0x26, 0xff), # 14: Green
    (0x39, 0x9d, 0xa0, 0xff), # 15: Teal

    (0x00, 0x00, 0x00, 0xff), # 0: Black
    (0x74, 0xfb, 0xfd, 0xff), # 1: Cyan
    (0xf0, 0x59, 0xf9, 0xff), # 2: Magenta
    (0xff, 0xff, 0xff, 0xff), # 3: White
"""

def ega_to_cga(img: PIL.Image.Image) -> PIL.Image.Image:
    if img.mode == 'RGB':
        ega_palette = tools.ega.PALETTE
        cga_palette = tools.cga.PALETTE
        color_mapping = _EGA_TO_CGA
    elif img.mode == 'RGBA':
        ega_palette = tools.ega.ONE_BIT_PALETTE
        cga_palette = tools.cga.ONE_BIT_PALETTE
        color_mapping = _EGA_TO_CGA_ONE_BIT
    else:
        raise ValueError(f'Unsupported image mode: `{img.mode}`. Expected `RGB` or `RGBA`.')

    w, h = img.size
    src = img.load()

    out = PIL.Image.new(img.mode, (w, h))
    dst = out.load()

    for y in range(h):
        for x in range(w):
            p = src[x, y]
            if img.mode == 'RGB':
                p_rgba = (p[0], p[1], p[2], 255)
            else:
                p_rgba = p
            assert p_rgba in ega_palette, f'Non-EGA-palette color at ({x}, {y}): {p}.'
            color_index = ega_palette.index(p_rgba)
            dst[x, y] = cga_palette[color_mapping[color_index]]

    return out
