import enum


class ScenarioBlock(enum.Enum):
    EXPERIENCE = 0
    ITEM = 1
    MONSTER = 4
    NPC = 5


def decode(data: bytes, disk: bytes) -> list[bytes | list[bytes]]:
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
    # FIXME move it to corresponding module
    assert len(results[ScenarioBlock.EXPERIENCE.value]) == 0x0e * 4 * 16, 'EXPERIENCE block size must be 0x0e * 4 * 16.'
    assert len(results[ScenarioBlock.ITEM.value]) % 0x4a == 0, 'ITEM block size must be multiple of 0x4a.'
    assert len(results[ScenarioBlock.MONSTER.value]) % 0xde == 0, 'MONSTER block size must be multiple of 0xde.'
    assert len(results[ScenarioBlock.NPC.value]) % 0x8e == 0, 'NPC block size must be multiple of 0x8e.'
    for block, record_size in [
        (ScenarioBlock.EXPERIENCE, 0x40),
        (ScenarioBlock.ITEM, 0x4a),
        (ScenarioBlock.MONSTER, 0xde),
        (ScenarioBlock.NPC, 0x8e),
    ]:
        block_data = results[block.value]
        records = [block_data[i:i+record_size] for i in range(0, len(block_data), record_size)]
        results[block.value] = records
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
        if isinstance(scenario, bytes):
            with open(f'unpacked/SCENARIO.{i}.DBS', 'wb') as f:
                f.write(scenario)
        else:
            records_size = len(scenario)
            digits = len(str(records_size-1))
            for j, record in enumerate(scenario):
                j = str(j).rjust(digits, '0')
                with open(f'unpacked/SCENARIO.{i}.{j}.DBS', 'wb') as f:
                    f.write(record)
