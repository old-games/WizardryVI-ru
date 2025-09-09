def decode(data: bytes, disk: bytes) -> list[bytes]:
    assert len(disk) >= 0x2c
    assert disk[:4] == b'\x00'*4
    offsets = [int.from_bytes(disk[i:i+4], 'little') for i in range(4, 0x2c, 4)]
    for i, offset in enumerate(offsets):
        assert offset <= len(data), f'Offset {offset} is out of range (disk size {len(data)}).'
    offsets.append(len(data))
    assert offsets == sorted(offsets), 'Offsets must be sorted.'
    results = []
    for i in range(len(offsets)-1):
        start = offsets[i]
        end = offsets[i+1]
        results.append(data[start:end])
    return results


if __name__ == '__main__':
    import os

    scenario_path = 'original/SCENARIO.DBS'
    disk_path = 'original/DISK.HDR'
    with open(scenario_path, 'rb') as f:
        scenario_data = f.read()
    with open(disk_path, 'rb') as f:
        disk_data = f.read()
    scenarios = decode(scenario_data, disk_data)
    os.makedirs('unpacked', exist_ok=True)
    for i, scenario in enumerate(scenarios):
        with open(f'unpacked/SCENARIO.{i}.DBS', 'wb') as f:
            f.write(scenario)
