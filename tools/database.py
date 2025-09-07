import tools.huffman


def reindex(data: dict[int, bytes], indices: bytes) -> dict[int, bytes]:
    if len(indices) < 2 or (len(indices) - 2) % 6 != 0:
        raise ValueError('Indices must be 2 + N*6 bytes')

    size = int.from_bytes(indices[:2], 'little')
    assert len(indices) >= size * 6 + 2, 'Indices length does not match expected size'
    assert set(indices[size*6+2:]) in ({0}, set()), 'Indices can end with zero padding bytes'

    def next_offset_iter(offset: int, data: dict[int, bytes]) -> int:
        # FIXME
        it = iter(data)
        while next(it) != offset:
            pass
        return it

    result = {}
    offset = None
    for i in range(size):
        entry = indices[2 + i*6 : 2 + (i+1)*6]
        start_id = int.from_bytes(entry[0:2], 'little')
        start_offset = int.from_bytes(entry[2:4], 'little')
        assert start_offset & 0xfc00 == 0
        extra_size = int.from_bytes(entry[4:5], 'little')
        high_offset = int.from_bytes(entry[5:6], 'little')
        start_offset |= high_offset << 10
        offset_iter = next_offset_iter(start_offset, data)
        if offset is not None:
            assert offset == start_offset, f'Offset mismatch: {offset} != {start_offset}'
        offset = start_offset
        for j in range(extra_size + 1):
            if offset not in data:
                raise KeyError(f'ID {start_id + j}, offset {offset} not found in data, index {len(result)} of {len(data)}')
            result[start_id + j] = data[offset]
            offset = next(offset_iter)

    return result


def decode(data: bytes, huffman_table: bytes) -> dict[int, bytes]:
    if len(huffman_table) != 1024:
        raise ValueError('Table must be exactly 1024 bytes')

    results = {}
    offset = 0
    errors = []
    while offset < len(data):
        huff_len = data[offset]
        length = data[offset + 1]
        if offset == 0x13d7a and huff_len == 0x8b:
            # This entry (`8b09db506c`) is broken.
            # It actually happened because this file was never truncated, so last entries may become
            # multiple tails merged together.
            # This was part of `@!T O   B E   C O N T I N U E D` originally.
            # Basically we shall not read file all the way, but only parts of it, following indices.
            offset -= 2
            huff_len = 5
            length = 8
            huff_len = 0x13d7f-offset-1
        huff_data = data[offset + 2:offset + 1 + huff_len]
        if length == 36 and huff_len == 23 and len(data) == 0x14000 and offset + 1 + huff_len == 0x14002:
            # This entry is a (stripped) copy of one of the previous entries, we can skip it.
            offset = 0x14000
            continue
        assert len(huff_data) + 1 == huff_len, f'Expected {huff_len} bytes, got {len(huff_data)+1} at offset {offset}'
        try:
            decoded = tools.huffman.decode(huff_data, huffman_table, length)
            assert len(decoded) == length, f'Decoded length {len(decoded)} does not match expected {length} at offset {offset}'
            results[offset] = decoded
        except Exception as e:
            errors.append(e)
        offset += 1 + huff_len

    assert offset == len(data), f"Offset {offset} does not match data length {len(data)}"

    if errors:
        raise errors[0]

    return results


def decode_plain(data: bytes, indices: bytes) -> dict[int, bytes]:
    if len(indices) < 2 or (len(indices) - 2) % 6 != 0:
        raise ValueError('Indices must be 2 + N*6 bytes')

    size = int.from_bytes(indices[:2], 'little')
    assert len(indices) >= size * 6 + 2, 'Indices length does not match expected size'
    assert set(indices[size*6+2:]) in ({0}, set()), 'Indices can end with zero padding bytes'

    def next_offset_iter(offset: int, data: dict[int, bytes]) -> int:
        # FIXME
        it = iter(data)
        while next(it) != offset:
            pass
        return it

    result = {}
    offset = None
    for i in range(size):
        entry = indices[2 + i*6 : 2 + (i+1)*6]
        start_id = int.from_bytes(entry[0:2], 'little')
        start_offset = int.from_bytes(entry[2:4], 'little')
        assert start_offset & 0xfc00 == 0
        extra_size = int.from_bytes(entry[4:5], 'little')
        high_offset = int.from_bytes(entry[5:6], 'little')
        start_offset |= high_offset << 10
        offset_iter = next_offset_iter(start_offset, data)
        if offset is not None:
            assert offset == start_offset, f'Offset mismatch: {offset} != {start_offset}'
        offset = start_offset
        for j in range(extra_size + 1):
            if offset not in data:
                raise KeyError(f'ID {start_id + j}, offset {offset} not found in data, index {len(result)} of {len(data)}')
            result[start_id + j] = data[offset]
            offset = next(offset_iter)

    return result
