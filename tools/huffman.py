def decode(data: bytes, table: bytes, length: int) -> bytes:
    if len(table) != 1024:
        raise ValueError('Table must be exactly 1024 bytes')

    output = bytearray()
    bit_pos = 0
    total_bits = len(data) * 8
    root = 0
    left = int.from_bytes(table[root * 4:root * 4 + 2], 'little', signed=True)
    right = int.from_bytes(table[root * 4 + 2:root * 4 + 4], 'little', signed=True)

    while bit_pos < total_bits and len(output) < length:
        node = root
        path = []
        while True:
            if bit_pos >= total_bits:
                break
            byte_idx = bit_pos // 8
            bit_idx = bit_pos % 8
            # Read bits MSB-first in each byte
            bit = (data[byte_idx] >> (7 - bit_idx)) & 1
            path.append(str(bit))

            left = int.from_bytes(table[node * 4:node * 4 + 2], 'little', signed=True)
            right = int.from_bytes(table[node * 4 + 2:node * 4 + 4], 'little', signed=True)
            next_node = left if bit == 0 else right

            bit_pos += 1

            if next_node >= 0:
                symbol = next_node
                output.append(symbol)
                break
            else:
                node = (-next_node) & 0xff

    assert len(output) == length, f'Decoded length {len(output)} does not match expected {length}'
    assert total_bits - bit_pos < 8, f'Excess bits after decoding `{bytes(output).decode("ascii")}`: {total_bits - bit_pos} bits remaining'

    return bytes(output)
