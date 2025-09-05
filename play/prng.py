import random
import time


"""
Variation of Wichmann-Hill algorithm for pseudo-random number generation used in Wizardry VI.
"""


def _update_rng(word_11D3B, word_11D3D, word_11D3F):
    # First sequence
    ax = word_11D3B
    bx = 0x177  # 375
    q, dx = divmod(ax, bx)
    cx = dx
    dx = 2
    ax = cx * dx
    bx = ax
    ax = 171 * cx
    ax = ax - bx
    if ax < 0:
        ax += 30269
    word_11D3B = ax

    # Second sequence
    ax = word_11D3D
    bx = 0x176  # 374
    q, dx = divmod(ax, bx)
    cx = dx
    dx = 0x23  # 35
    ax = cx * dx
    bx = ax
    ax = 172 * cx
    ax = ax - bx
    if ax < 0:
        ax += 30307
    word_11D3D = ax

    # Third sequence
    ax = word_11D3F
    bx = 0x178  # 376
    q, dx = divmod(ax, bx)
    cx = dx
    dx = 0x63  # 99
    ax = cx * dx
    bx = ax
    ax = 170 * cx
    ax = ax - bx
    if ax < 0:
        ax += 30323
    word_11D3F = ax

    return word_11D3B, word_11D3D, word_11D3F

def prng_value():
    global word_11D3B, word_11D3D, word_11D3F

    # Call the update function (sub_125B9)
    word_11D3B, word_11D3D, word_11D3F = _update_rng(word_11D3B, word_11D3D, word_11D3F)

    # First part
    ax = word_11D3B
    dx = 0
    bx = 30269
    q, dx = divmod(ax, bx)
    ax = 10000
    ax = ax * dx
    bx = 30269
    q, ax = divmod(ax, bx)
    ax = ax & 0x7FFF
    cx = ax

    # Second part
    ax = word_11D3D
    dx = 0
    bx = 30307
    q, dx = divmod(ax, bx)
    ax = 10000
    ax = ax * dx
    bx = 30307
    q, ax = divmod(ax, bx)
    ax = ax & 0x7FFF
    cx = (cx + ax) & 0x7FFF

    # Third part
    ax = word_11D3F
    dx = 0
    bx = 30323
    q, dx = divmod(ax, bx)
    ax = 10000
    ax = ax * dx
    bx = 30323
    q, ax = divmod(ax, bx)
    ax = ax & 0x7FFF
    ax = (ax + cx) & 0x7FFF

    return ax

word_11D3B, word_11D3D, word_11D3F = 3000, 1, 29999

TICKS_PER_SECOND = 1193182 / 65536  # ≈18.2065

def dos_ticks_2byte():
    # There are ~18.2065 ticks per second in DOS
    now = time.localtime()
    seconds_since_midnight = (
        now.tm_hour * 3600 +
        now.tm_min * 60 +
        now.tm_sec
    )
    # Add fractions of a second for more accuracy
    fractional = time.time() % 1
    ticks = int((seconds_since_midnight + fractional) * TICKS_PER_SECOND)
    # Return as 2-byte value (like a 16-bit unsigned int)
    return ticks & 0xFFFF

def seed(time=None, from_dos_time=True):
    global word_11D3B, word_11D3D, word_11D3F
    if time is not None:
        word_11D3D = (time + 2) % 0xffff
    elif from_dos_time:
        word_11D3D = (dos_ticks_2byte() + 2) % 0xffff
    else:
        word_11D3B, word_11D3D, word_11D3F = 3000, 1, 29999


def test_skills():
    used = set()
    r = []
    while True:
        for i in range(3):
            val = prng_value()
            skill = val % 7
            if skill not in used:
                break
        if skill not in used:
            used.add(skill)
            r.append(skill)
        if prng_value() % 2 == 0:
            break
    return sorted(r)


def test_average(runs=100000, with_reseed=False):
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(runs):
        if with_reseed and i % 100 == 0:
            seed(from_dos_time=False)
            for _ in range(random.randint(1, 100)):
                prng_value()
            seed(from_dos_time=False, time=random.randint(0, 0xffff))
        skills = test_skills()
        for skill in skills:
            counts[skill] = counts.get(skill, 0) + 1
    print(', '.join(f'{k/runs*100:.2f}%' for k in counts.values()))


def test_average_seven(runs=100000):
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(runs):
        v = prng_value() % 7
        counts[v] = counts.get(v, 0) + 1
    print(', '.join(f'{k/runs*100:.2f}%' for k in counts.values()))


print(test_skills())
test_average()

seed(from_dos_time=False)

test_average_seven()

print('---')

seed(from_dos_time=False)
seed(from_dos_time=True)

print(test_skills())
test_average()

seed(from_dos_time=False)
seed(from_dos_time=True)

test_average_seven()

print('---')

seed(from_dos_time=False)
seed(from_dos_time=False, time=45678)

print(test_skills())
test_average()


seed(from_dos_time=False)
seed(from_dos_time=False, time=45678)

test_average_seven()

print('---')

seed(from_dos_time=False)
seed(from_dos_time=False, time=12345)

print(test_skills())
test_average()

seed(from_dos_time=False)
seed(from_dos_time=False, time=12345)

test_average_seven()

print('---')

test_average(with_reseed=True, runs=100000)
