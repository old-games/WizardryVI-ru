import itertools

import tools.huffman


def encode(messages: dict[int, bytes]) -> tuple[bytes, bytes, bytes]:
    '''
    Encode messages using the database format (indexed).
    Returns (data, indices, huffman_table).
    '''

    # Build Huffman table from all message bytes
    all_bytes = b''.join(messages.values())
    huffman_table = tools.huffman.table(all_bytes)
    assert len(huffman_table) <= 1024, 'Huffman table must be not greater than 1024 bytes.'
    huffman_table = huffman_table.ljust(1024, b'\x00')

    # Encode each message.
    offsets = []
    data_blocks = []
    offset = 0
    for msg_id in sorted(messages):
        msg = messages[msg_id]
        encoded = tools.huffman.encode(msg, huffman_table)
        huff_len = len(encoded) + 1 # `+1` for length byte.
        length = len(msg)
        block = bytes([huff_len, length]) + encoded
        data_blocks.append(block)
        offsets.append((msg_id, offset))
        offset += len(block)

    data_file = b''.join(data_blocks)

    # Build indices in blocks of consecutive IDs.
    count = 0
    indices = b''
    for k, group in itertools.groupby(enumerate(offsets), lambda x: x[1][0] - x[0]):
        group = list(group)
        start_id = group[0][1][0]
        start_offset = group[0][1][1]
        extra_size = len(group) - 1
        high_offset = (start_offset >> 10) & 0xff
        indices += start_id.to_bytes(2, 'little')
        indices += (start_offset & 0x3ff).to_bytes(2, 'little')
        indices += extra_size.to_bytes(1, 'little')
        indices += high_offset.to_bytes(1, 'little')
        count += 1

    indices = count.to_bytes(2, 'little') + indices

    return data_file, indices, huffman_table


if __name__ == '__main__':
    import json
    import sys

    language = sys.argv[1] if len(sys.argv) > 1 else 'en'
    encoding = {'en': 'ascii', 'ru': 'cp866'}[language]

    def remove_fixme(s):
        if s.startswith('FIXME'):
            return s[5:]
        return s

    # Load messages from JSON.
    with open('messages/messages.json', 'r') as f:
        messages = {int(k): remove_fixme(v[language]).encode(encoding) for k, v in json.load(f).items()}

    data, indices, huffman_table = encode(messages)

    with open('MSG.DBS', 'wb') as f:
        f.write(data)
    with open('MSG.HDR', 'wb') as f:
        f.write(indices)
    with open('MISC.HDR', 'wb') as f:
        f.write(huffman_table)
