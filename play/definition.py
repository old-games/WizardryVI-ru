import itertools
from enum import Enum, auto


class CharacterClass(Enum):
    FIGHTER = auto()
    MAGE = auto()
    PRIEST = auto()
    THIEF = auto()
    RANGER = auto()
    ALCHEMIST = auto()
    BARD = auto()
    PSIONIC = auto()
    VALKYRIE = auto()
    BISHOP = auto()
    SAMURAI = auto()
    MONK = auto()
    NINJA = auto()
    LORD = auto()

def get_level_experience(character_class, level):
    if level < 1 or not isinstance(level, int):
        raise RuntimeError("Invalid level.")

    elif level <= 11:
        match character_class:
            case CharacterClass.FIGHTER:
                return [None, 0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000][level]
            case CharacterClass.MAGE:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case CharacterClass.PRIEST:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case CharacterClass.THIEF:
                return [None, 0, 900, 1800, 3600, 7200, 14400, 28800, 57600, 115200, 230400, 460800][level]
            case CharacterClass.RANGER:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case CharacterClass.ALCHEMIST:
                return [None, 0, 1100, 2200, 4400, 8800, 17600, 35200, 70400, 140800, 281600, 563200][level]
            case CharacterClass.BARD:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case CharacterClass.PSIONIC:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case CharacterClass.VALKYRIE:
                return [None, 0, 1100, 2200, 4400, 8800, 17600, 35200, 70400, 140800, 281600, 563200][level]
            case CharacterClass.BISHOP:
                return [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000][level]
            case CharacterClass.SAMURAI:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case CharacterClass.MONK:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case CharacterClass.NINJA:
                return [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000][level]
            case CharacterClass.LORD:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case _:
                raise RuntimeError(f"Unknown character class: {character_class}.")

    else:
        match character_class:
            case CharacterClass.FIGHTER:
                after_eleven = 256000
            case CharacterClass.MAGE:
                after_eleven = 375000
            case CharacterClass.PRIEST:
                after_eleven = 375000
            case CharacterClass.THIEF:
                after_eleven = 225000
            case CharacterClass.RANGER:
                after_eleven = 415000
            case CharacterClass.ALCHEMIST:
                after_eleven = 312000
            case CharacterClass.BARD:
                after_eleven = 375000
            case CharacterClass.PSIONIC:
                after_eleven = 375000
            case CharacterClass.VALKYRIE:
                after_eleven = 312000
            case CharacterClass.BISHOP:
                after_eleven = 445000
            case CharacterClass.SAMURAI:
                after_eleven = 415000
            case CharacterClass.MONK:
                after_eleven = 415000
            case CharacterClass.NINJA:
                after_eleven = 475000
            case CharacterClass.LORD:
                after_eleven = 415000
            case _:
                raise RuntimeError(f"Unknown character class: {character_class}.")

        return get_level_experience(character_class, 11) + (level-11) * after_eleven

def get_level_by_experience(character_class: CharacterClass, experience: int) -> int:
    if experience < 0:
        raise RuntimeError("Experience must be non-negative.")

    for level in itertools.count(1):
        exp_needed = get_level_experience(character_class, level + 1)
        if experience < exp_needed:
            return level
