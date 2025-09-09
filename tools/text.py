OGR001 = {
      1: 229,
      2: 166,
      3: 237,
      4: 161,
      5: 238,
      9: 149,
     11: 134,
     12: 157,
     13: 129,
     14: 158,
     35: 158,
     36: 134,
     38: 149,
     61: 157,
     65: 148,
     66: 136,
     67: 145,
     68: 130,
     69: 147,
     70: 128,
     71: 143,
     72: 144,
     73: 152,
     74: 142,
     75: 139,
     76: 132,
     77: 156,
     78: 146,
     79: 153,
     80: 135,
     81: 137,
     82: 138,
     83: 155,
     84: 133,
     85: 131,
     86: 140,
     87: 150,
     88: 151,
     89: 141,
     90: 159,
     94: 129,
     97: 228,
     98: 168,
     99: 225,
    100: 162,
    101: 227,
    102: 160,
    103: 175,
    104: 224,
    105: 232,
    106: 174,
    107: 171,
    108: 164,
    109: 236,
    110: 226,
    111: 233,
    112: 167,
    113: 169,
    114: 170,
    115: 235,
    116: 165,
    117: 163,
    118: 172,
    119: 230,
    120: 231,
    121: 173,
    122: 239,
}

OGR001_REVERSED = {v: k for k, v in sorted(OGR001.items())}


def encode_one_all_alternatives(symbol: str, encoding: str) -> list[bytes]:
    '''
    Encode a string into a list of bytes using the specified encoding.
    Each character is encoded separately, resulting in a list of bytes.
    Supported encodings: 'ascii', 'cp866', 'ogr001'.
    '''
    if encoding in ('ascii', 'cp866'):
        return [symbol.encode(encoding)]
    elif encoding == 'ogr001':
        table = OGR001
    else:
        raise ValueError(f'Unsupported encoding: {encoding}.')

    result = []
    for k, v in table.items():
        if v == ord(symbol.encode('cp866')):
            result.append(bytes([k]))
    return result


def encode(data: str, encoding: str) -> bytes:
    '''
    Encode a string into bytes using the specified encoding.
    Supported encodings: 'ascii', 'cp866', 'ogr001'.
    '''
    if encoding in ('ascii', 'cp866'):
        return data.encode(encoding)
    elif encoding == 'ogr001':
        table = OGR001_REVERSED
    else:
        raise ValueError(f'Unsupported encoding: {encoding}.')

    result = []
    for ch in data:
        code = ord(ch.encode('cp866'))
        if code in table:
            result.append(table[code])
        else:
            result.append(ord(ch.encode('ascii')))
    return bytes(result)


def decode(data: bytes, encoding: str) -> str:
    '''
    Decode a bytes object (data) into a string using the specified encoding.
    Supported encodings: 'ascii', 'cp866', 'ogr001'.
    '''
    if encoding in ('ascii', 'cp866'):
        return data.decode(encoding)
    elif encoding == 'ogr001':
        table = OGR001
    else:
        raise ValueError(f'Unsupported encoding: {encoding}.')

    result = []
    for b in data:
        if b in table:
            result.append(bytes([table[b]]).decode('cp866'))
        else:
            result.append(bytes([b]).decode('ascii'))
    return ''.join(result)
