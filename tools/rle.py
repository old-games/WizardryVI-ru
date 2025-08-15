def decompress(data: bytes) -> bytes:
    result = bytearray()
    i = 0
    data_len = len(data)
    while i < data_len:
        x = data[i]
        i += 1
        if i % 0x1000 == 0:
            # Padding.
            continue
        if x < 0x80:
            if i + x > data_len:
                raise ValueError(f'Unexpected end of data at {i} for literal run of {x} bytes')
            result.extend(data[i:i+x])
            i += x
            continue
        if x != 0:
            if i >= data_len:
                raise ValueError(f'Unexpected end of data at {i} for RLE run')
            o = data[i:i+1]
            i += 1
            result.extend(o * (0x100 - x))
    return bytes(result)
