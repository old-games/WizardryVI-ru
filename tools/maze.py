def decode(data: bytes) -> tuple[list[tuple[int, int, bytes]], list[tuple[int, int, int, int, int]]]:
    assert len(data) >= 4
    data_entries = int.from_bytes(data[0:2], 'little')
    object_entries = int.from_bytes(data[2:4], 'little')
    assert len(data) >= 4 + (data_entries + object_entries) * 5
    tail = data[4 + (data_entries + object_entries) * 5:]
    data_table = data[4:4 + data_entries * 5]
    object_table = data[4 + data_entries * 5:4 + (data_entries + object_entries) * 5]
    if data_table[-1]*data_table[-2]*2 + data_table[-3] + data_table[-4]*0x1000 + data_table[-5]*0x10 == len(tail):
        bpp = 2
    else:
        bpp = 4
    assert data_table[-1]*data_table[-2]*bpp + data_table[-3] + data_table[-4]*0x1000 + data_table[-5]*0x10 == len(tail)
    assert len(tail) % 4 == 0
    it = iter(data[4:])
    next_offset = 0
    data_payload = []
    for _ in range(data_entries):
        paragraph = next(it) | (next(it) << 8)
        offset = next(it)
        w = next(it)
        h = next(it)
        assert w > 0
        assert h > 0
        assert offset < 0x10
        size = w*h*bpp
        data_payload.append((w*8, h, tail[next_offset:next_offset+size]))
        assert next_offset == paragraph*0x10 + offset
        next_offset += size
    assert next_offset == len(tail)
    object_table = []
    for i in range(0, object_entries*5, 5):
        entry = data[4+data_entries*5+i:4+data_entries*5+i+5]
        texture_id = entry[0]
        assert texture_id < len(data_payload)
        width = entry[4]*8
        x = entry[1]
        y = entry[2]
        texture_x = entry[3]*8
        assert width <= data_payload[texture_id][0]
        assert texture_x + width <= data_payload[texture_id][0]
        object_table.append((texture_id, x, y, texture_x, width))
    return data_payload, object_table


def encode(data_table: list[tuple[int, int, bytes]], object_table: list[tuple[int, int, int, int, int]]) -> bytes:
    data_entries = len(data_table)
    object_entries = len(object_table)
    result = bytearray()
    result.extend(data_entries.to_bytes(2, 'little'))
    result.extend(object_entries.to_bytes(2, 'little'))
    data_offset = 0
    for w, h, data in data_table:
        assert w % 8 == 0
        paragraph = data_offset // 0x10
        offset = data_offset % 0x10
        assert offset < 0x10
        result.extend(paragraph.to_bytes(2, 'little'))
        result.append(offset)
        result.append(w//8)
        result.append(h)
        data_offset += len(data)
    for texture_id, x, y, texture_x, width in object_table:
        assert texture_id < data_entries
        assert width % 8 == 0
        assert texture_x % 8 == 0
        assert texture_x + width <= data_table[texture_id][0]
        result.append(texture_id)
        result.append(x)
        result.append(y)
        result.append(texture_x//8)
        result.append(width//8)
    for w, h, data in data_table:
        assert w % 8 == 0
        result.extend(data)
    return bytes(result)
