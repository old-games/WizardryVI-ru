def decode(data: bytes, size: int) -> list[bytes]:
    result = []
    for i in range(0, len(data), size):
        result.append(data[i:i+size])
    return result
