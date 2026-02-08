'''
     CGA:             EGA/T16:
0099 0d00 28 00 0e    0d00 28 00 0e
009a 1001 34 00 08    1001 34 00 08
009b 1202 3c 00 04    1202 3c 00 04
009c 0000 08 00 00    0000 08 00 00
009d 0801 34 01 04    0801 34 01 04
009e 0e02 3c 00 02    0e02 3c 00 02
009f ff00 28 0a 04    ff00 28 0a 04
00a0 0801 34 05 03    0801 34 05 03
00a1 0e02 3c 02 02    0e02 3c 02 02
00a2 1b00 28 00 04    1b00 28 00 04
00a3 1801 34 00 03    1801 34 00 03
...
'''

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
