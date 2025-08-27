import tools.huffman


def decode(data: bytes):
    assert len(data) >= 2
    table_size = int.from_bytes(data[:2], 'little')
    assert len(data) >= 2 + table_size
    huffman_table = data[2:2+table_size]
    compressed_data = data[2+table_size:]
    if table_size == 0:
        return compressed_data
    else:
        return tools.huffman.decode(compressed_data, huffman_table, length=None)
