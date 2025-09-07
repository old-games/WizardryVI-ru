import collections
import heapq


def decode(data: bytes, table: bytes, length: int | None) -> bytes:
    assert len(table) > 0, 'Huffman table is empty.'
    output = bytearray()
    bit_pos = 0
    total_bits = len(data) * 8
    root = 0
    left = int.from_bytes(table[root * 4:root * 4 + 2], 'little', signed=True)
    right = int.from_bytes(table[root * 4 + 2:root * 4 + 4], 'little', signed=True)

    while bit_pos < total_bits and (length is None or len(output) < length):
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

    assert length is None or len(output) == length, f'Decoded length {len(output)} does not match expected {length}.'
    assert total_bits - bit_pos < 8, f'Excess bits after decoding `{bytes(output).decode("ascii")}`: {total_bits - bit_pos} bits remaining.'

    return bytes(output)


def table(data: bytes) -> bytes:
    '''
    Generate the optimal Huffman table for the given input data.
    Returns the table in the same binary format as expected by decode().
    '''
    # Count symbol frequencies
    freq = collections.Counter(data)
    if not freq:
        return b''

    # Build Huffman tree: (freq, node_id, left, right, symbol)
    heap = []
    node_id = 0
    nodes = {}

    for symbol, count in freq.items():
        heap.append((count, node_id, None, None, symbol))
        nodes[node_id] = (None, None, symbol)
        node_id += 1

    heapq.heapify(heap)
    next_id = node_id

    while len(heap) > 1:
        f1, id1, l1, r1, s1 = heapq.heappop(heap)
        f2, id2, l2, r2, s2 = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next_id, id1, id2, None))
        nodes[next_id] = (id1, id2, None)
        next_id += 1

    # Map node ids to table indices
    # Table: for each node, 4 bytes: left (2 bytes, signed), right (2 bytes, signed)
    # If child is a leaf: value >= 0 (symbol)
    # If child is a node: value < 0, -node_id
    table_map = {}
    def assign_indices(node_id, idx=0):
        table_map[node_id] = idx
        left, right, symbol = nodes[node_id]
        next_idx = idx + 1
        if left is not None and nodes[left][2] is None:
            next_idx = assign_indices(left, next_idx)
        if right is not None and nodes[right][2] is None:
            next_idx = assign_indices(right, next_idx)
        return next_idx

    root_id = heap[0][1]
    assign_indices(root_id)

    # Build table
    table = bytearray()
    for node_id in sorted(table_map, key=lambda k: table_map[k]):
        left, right, symbol = nodes[node_id]
        for child in (left, right):
            if child is None:
                # Should not happen
                table += (0).to_bytes(2, 'little', signed=True)
            elif nodes[child][2] is not None:
                # Leaf: symbol value
                table += (nodes[child][2]).to_bytes(2, 'little', signed=True)
            else:
                # Internal node: -table index
                table += (-table_map[child]).to_bytes(2, 'little', signed=True)

    return bytes(table)


def encode(data: bytes, table: bytes) -> bytes:
    """
    Encode data using the provided Huffman table.
    Returns the compressed bitstream as bytes.
    """
    # Build codebook: symbol -> bitstring
    codebook = {}
    queue = collections.deque([(0, '')])  # (node_idx, bitstring)
    while queue:
        node, bits = queue.popleft()
        left = int.from_bytes(table[node * 4:node * 4 + 2], 'little', signed=True)
        right = int.from_bytes(table[node * 4 + 2:node * 4 + 4], 'little', signed=True)
        for bit, child in [(0, left), (1, right)]:
            if child >= 0:
                codebook[child] = bits + str(bit)
            else:
                queue.append(((-child) & 0xff, bits + str(bit)))
    # Encode message
    bitstring = ''
    for b in data:
        bitstring += codebook[b]
    # Pad to full bytes
    while len(bitstring) % 8 != 0:
        bitstring += '0'
    # Convert to bytes
    encoded = int(bitstring, 2).to_bytes(len(bitstring) // 8, 'big') if bitstring else b''
    return encoded
