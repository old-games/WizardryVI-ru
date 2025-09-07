def decode(data: bytes, size: int) -> list[bytes]:
    result = []
    for i in range(0, len(data), size):
        result.append(data[i:i+size])
    return result


def encode(symbols: list[bytes]) -> bytes:
    '''
    Concatenate a list of byte strings (symbols) into a single bytes object.
    '''
    return b''.join(symbols)


if __name__ == '__main__':
    import os

    from PIL import Image

    import tools.cga
    import tools.ega
    import tools.tandy

    os.makedirs('output', exist_ok=True)

    # Font config: (font_type, subdir, font_num, encode_func, symbol_size, w, h)
    font_configs = [
        # Tandy
        ('.T16', 'tandy', 0, tools.tandy.encode_one_bit, 32, 8, 8),
        ('.T16', 'tandy', 1, tools.tandy.encode,         32, 8, 8),
        ('.T16', 'tandy', 2, tools.tandy.encode,         32, 8, 8),
        ('.T16', 'tandy', 3, tools.tandy.encode,         32, 8, 8),
        ('.T16', 'tandy', 4, tools.tandy.encode,         32, 8, 8),
        # CGA
        ('.CGA', 'cga',   0, tools.cga.encode_one_bit,              16, 8, 8),
        ('.CGA', 'cga',   1, tools.cga.encode_without_interleaving, 16, 8, 8),
        ('.CGA', 'cga',   2, tools.cga.encode_without_interleaving, 16, 8, 8),
        ('.CGA', 'cga',   3, tools.cga.encode_without_interleaving, 16, 8, 8),
        ('.CGA', 'cga',   4, tools.cga.encode_without_interleaving, 16, 8, 8),
        # EGA
        ('.EGA', 'ega',   0, tools.ega.encode_one_bit,  8, 8, 8),
        ('.EGA', 'ega',   1, tools.ega.encode,         32, 8, 8),
        ('.EGA', 'ega',   2, tools.ega.encode,         32, 8, 8),
        ('.EGA', 'ega',   3, tools.ega.encode,         32, 8, 8),
        ('.EGA', 'ega',   4, tools.ega.encode,         32, 8, 8),
    ]

    for font_type, subdir, font_num, encode_func, symbol_size, w, h in font_configs:
        prefix = f'WFONT{font_num}{font_type}.'
        symbols = []
        for idx in range(128):
            fname = f'{prefix}{idx:03d}.png'
            fpath = os.path.join(subdir, 'fonts', fname)
            if not os.path.exists(fpath):
                raise FileNotFoundError(f'Missing symbol PNG: {fpath}')
            img = Image.open(fpath).convert('RGBA').resize((w, h), Image.NEAREST)
            encoded = encode_func(img)
            if len(encoded) != symbol_size:
                raise ValueError(f'Encoded symbol size mismatch for {fname}: got {len(encoded)}, expected {symbol_size}')
            symbols.append(encoded)
        # Add upper 128 symbols only for fonts 0 and 3
        #if font_num in (0,):# 3):
        symbols += [symbols[24]] * 128
        out_data = b''.join(symbols)
        out_fname = f'WFONT{font_num}{font_type}'
        with open(out_fname, 'wb') as f:
            f.write(out_data)
