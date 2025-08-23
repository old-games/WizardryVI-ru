import enum
import itertools


class Parameter(enum.Enum):
    STRENGTH = enum.auto()
    INTELLIGENCE = enum.auto()
    PIETY = enum.auto()
    VITALITY = enum.auto()
    DEXTERITY = enum.auto()
    SPEED = enum.auto()
    PERSONALITY = enum.auto()


class Race(enum.Enum):
    HUMAN = enum.auto()
    ELF = enum.auto()
    DWARF = enum.auto()
    GNOME = enum.auto()
    HOBBIT = enum.auto()
    FAERIE = enum.auto()
    LIZARDMAN = enum.auto()
    DRACON = enum.auto()
    FELPURR = enum.auto()
    RAWULF = enum.auto()
    MOOK = enum.auto()


class Class(enum.Enum):
    FIGHTER = enum.auto()
    MAGE = enum.auto()
    PRIEST = enum.auto()
    THIEF = enum.auto()
    RANGER = enum.auto()
    ALCHEMIST = enum.auto()
    BARD = enum.auto()
    PSIONIC = enum.auto()
    VALKYRIE = enum.auto()
    BISHOP = enum.auto()
    SAMURAI = enum.auto()
    MONK = enum.auto()
    NINJA = enum.auto()
    LORD = enum.auto()


class Spellbook(enum.Enum):
    NONE = enum.auto()
    PSIONIC = enum.auto()
    PRIEST = enum.auto()
    MAGE = enum.auto()
    ALCHEMIST = enum.auto()
    BISHOP = enum.auto() # == PRIEST + MAGE
    # NINJA ?


class SkillType(enum.Enum):
    WEAPONRY = enum.auto()
    PHYSICAL = enum.auto()
    ACADEMIA = enum.auto()


class Skill(enum.Enum):
    # Weaponry:
    WAND_AND_DAGGER = enum.auto()
    SWORD = enum.auto()
    AXE = enum.auto()
    MACE_AND_FLAIL = enum.auto()
    POLE_AND_STAFF = enum.auto()
    THROWING = enum.auto()
    SLING = enum.auto()
    BOWS = enum.auto()
    SHIELD = enum.auto()
    HANDS_AND_FEET = enum.auto()

    # Physical:
    SCOUTING = enum.auto()
    MUSIC = enum.auto()
    ORATORY = enum.auto()
    LEGERDEMAIN = enum.auto()
    SKULDUGGERY = enum.auto()
    NINJUTSU = enum.auto()

    # Academia:
    ARTIFACTS = enum.auto()
    MYTHOLOGY = enum.auto()
    SCRIBE = enum.auto()
    THEOSOPHY = enum.auto()
    THEOLOGY = enum.auto()
    ALCHEMY = enum.auto()
    THAUMATURGY = enum.auto()
    KIRIJUTSU = enum.auto()


POINTS_PROBABILITIES = {
    Race.HUMAN: [(7, 68), (5, 60), (8, 59), (10, 58), (6, 54), (9, 53), (17, 11), (14, 9), (15, 8), (18, 6), (13, 5), (16, 5)],
    Race.LIZARDMAN: [(5, 69), (7, 66), (9, 66), (6, 65), (8, 62), (10, 54), (16, 11), (14, 9), (13, 8), (17, 6), (15, 4), (18, 4), (22, 1)],
}


def get_level_experience(character_class: Class, level: int):
    if level < 1 or not isinstance(level, int):
        raise RuntimeError(f'Invalid level: {level}.')

    elif level <= 11:
        match character_class:
            case Class.FIGHTER:
                return [None, 0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000][level]
            case Class.MAGE:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case Class.PRIEST:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case Class.THIEF:
                return [None, 0, 900, 1800, 3600, 7200, 14400, 28800, 57600, 115200, 230400, 460800][level]
            case Class.RANGER:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case Class.ALCHEMIST:
                return [None, 0, 1100, 2200, 4400, 8800, 17600, 35200, 70400, 140800, 281600, 563200][level]
            case Class.BARD:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case Class.PSIONIC:
                return [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000][level]
            case Class.VALKYRIE:
                return [None, 0, 1100, 2200, 4400, 8800, 17600, 35200, 70400, 140800, 281600, 563200][level]
            case Class.BISHOP:
                return [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000][level]
            case Class.SAMURAI:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case Class.MONK:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case Class.NINJA:
                return [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000][level]
            case Class.LORD:
                return [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800][level]
            case _:
                raise RuntimeError(f'Unknown class: {character_class}.')

    else:
        match character_class:
            case Class.FIGHTER:
                after_eleven = 256000
            case Class.MAGE:
                after_eleven = 375000
            case Class.PRIEST:
                after_eleven = 375000
            case Class.THIEF:
                after_eleven = 225000
            case Class.RANGER:
                after_eleven = 415000
            case Class.ALCHEMIST:
                after_eleven = 312000
            case Class.BARD:
                after_eleven = 375000
            case Class.PSIONIC:
                after_eleven = 375000
            case Class.VALKYRIE:
                after_eleven = 312000
            case Class.BISHOP:
                after_eleven = 445000
            case Class.SAMURAI:
                after_eleven = 415000
            case Class.MONK:
                after_eleven = 415000
            case Class.NINJA:
                after_eleven = 475000
            case Class.LORD:
                after_eleven = 415000
            case _:
                raise RuntimeError(f'Unknown class: {character_class}.')

        return get_level_experience(character_class, 11) + (level-11) * after_eleven


def get_level_by_experience(character_class: Class, experience: int) -> int:
    if experience < 0:
        raise RuntimeError('Experience must be non-negative.')

    for level in itertools.count(1):
        exp_needed = get_level_experience(character_class, level + 1)
        if experience < exp_needed:
            return level


def get_race_parameters(race: Race) -> dict[Parameter, int]:
    if race == Race.HUMAN:
        params = [ 9,  8,  8,  9,  9,  8,  8]
    elif race == Race.ELF:
        params = [ 7, 10, 10,  7,  9,  9,  8]
    elif race == Race.DWARF:
        params = [11,  6, 10, 12,  7,  7,  7]
    elif race == Race.GNOME:
        params = [10,  7, 13, 10,  8,  6,  6]
    elif race == Race.HOBBIT:
        params = [ 8,  7,  6,  9, 10,  7, 13]
    elif race == Race.FAERIE:
        params = [ 5, 11,  6,  6, 10, 14, 12]
    elif race == Race.LIZARDMAN:
        params = [12,  5,  5, 14,  8, 10,  3]
    elif race == Race.DRACON:
        params = [10,  7,  6, 12, 10,  8,  6]
    elif race == Race.FELPURR:
        params = [ 7, 10,  7,  7, 10, 12, 10]
    elif race == Race.RAWULF:
        params = [ 8,  6, 12, 10,  8,  8, 10]
    elif race == Race.MOOK:
        params = [10, 10,  6, 10,  7,  7,  9]
    else:
        raise RuntimeError(f'Unknown race: {race}.')
    return dict(zip(
        (Parameter.STRENGTH, Parameter.INTELLIGENCE, Parameter.PIETY, Parameter.VITALITY, Parameter.DEXTERITY, Parameter.SPEED, Parameter.PERSONALITY),
        params,
    ))


def get_class_requirements(character_class: Class) -> dict[Parameter, int]:
    if character_class == Class.FIGHTER:
        return {Parameter.STRENGTH: 12}
    elif character_class == Class.MAGE:
        return {Parameter.INTELLIGENCE: 12}
    elif character_class == Class.PRIEST:
        return {Parameter.PIETY: 12, Parameter.PERSONALITY: 8}
    elif character_class == Class.THIEF:
        return {Parameter.DEXTERITY: 12, Parameter.SPEED: 8}
    elif character_class == Class.RANGER:
        return {Parameter.STRENGTH: 10, Parameter.INTELLIGENCE: 8, Parameter.PIETY: 8, Parameter.VITALITY: 11, Parameter.DEXTERITY: 10, Parameter.SPEED: 8, Parameter.PERSONALITY: 8}
    elif character_class == Class.ALCHEMIST:
        return {Parameter.INTELLIGENCE: 13, Parameter.DEXTERITY: 13}
    elif character_class == Class.BARD:
        return {Parameter.INTELLIGENCE: 10, Parameter.DEXTERITY: 12, Parameter.SPEED: 8, Parameter.PERSONALITY: 12}
    elif character_class == Class.PSIONIC:
        return {Parameter.STRENGTH: 10, Parameter.INTELLIGENCE: 14, Parameter.VITALITY: 14, Parameter.PERSONALITY: 10}
    elif character_class == Class.VALKYRIE:
        return {Parameter.STRENGTH: 10, Parameter.PIETY: 11, Parameter.VITALITY: 11, Parameter.DEXTERITY: 10, Parameter.SPEED: 11, Parameter.PERSONALITY: 8}
    elif character_class == Class.BISHOP:
        return {Parameter.INTELLIGENCE: 15, Parameter.PIETY: 15, Parameter.PERSONALITY: 8}
    elif character_class == Class.LORD:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE: 9, Parameter.PIETY: 12, Parameter.VITALITY: 12, Parameter.DEXTERITY: 9, Parameter.SPEED: 9, Parameter.PERSONALITY: 14}
    elif character_class == Class.SAMURAI:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE: 11, Parameter.VITALITY: 9, Parameter.DEXTERITY: 12, Parameter.SPEED: 14, Parameter.PERSONALITY: 8}
    elif character_class == Class.MONK:
        return {Parameter.STRENGTH: 13, Parameter.INTELLIGENCE: 8, Parameter.PIETY: 13, Parameter.DEXTERITY: 10, Parameter.SPEED: 13, Parameter.PERSONALITY: 8}
    elif character_class == Class.NINJA:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE: 10, Parameter.PIETY: 10, Parameter.VITALITY: 12, Parameter.DEXTERITY: 12, Parameter.SPEED: 12}
    else:
        raise RuntimeError(f'Unknown class: {character_class}.')


def get_class_skills(character_class: Class, skill_types: set[SkillType] | None = None) -> list[Skill]:
    result = list[Skill]()

    if character_class == Class.MONK:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.HANDS_AND_FEET,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
                Skill.NINJUTSU,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOSOPHY,
                Skill.KIRIJUTSU,
            ])

    elif character_class == Class.BISHOP:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.SLING,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOLOGY,
                Skill.THAUMATURGY,
            ])

    elif character_class == Class.LORD:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOLOGY,
            ])

    elif character_class == Class.NINJA:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
                Skill.HANDS_AND_FEET,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.LEGERDEMAIN,
                Skill.SKULDUGGERY,
                Skill.NINJUTSU,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.ALCHEMY,
                Skill.KIRIJUTSU,
            ])

    elif character_class == Class.SAMURAI:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THAUMATURGY,
                Skill.KIRIJUTSU,
            ])

    elif character_class == Class.VALKYRIE:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOLOGY,
            ])

    elif character_class == Class.PSIONIC:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOSOPHY,
            ])

    elif character_class == Class.PRIEST:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.SLING,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THEOLOGY,
            ])

    elif character_class == Class.THIEF:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
                Skill.LEGERDEMAIN,
                Skill.SKULDUGGERY,
                Skill.NINJUTSU,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
            ])

    elif character_class == Class.RANGER:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.LEGERDEMAIN,
                Skill.SKULDUGGERY,
                Skill.NINJUTSU,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.ALCHEMY,
            ])

    elif character_class == Class.BARD:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.MUSIC,
                Skill.ORATORY,
                Skill.LEGERDEMAIN,
                Skill.SKULDUGGERY,
                Skill.NINJUTSU,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THAUMATURGY,
            ])

    elif character_class == Class.ALCHEMIST:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.ALCHEMY,
            ])

    elif character_class == Class.MAGE:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
                Skill.ORATORY,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
                Skill.THAUMATURGY,
            ])

    elif character_class == Class.FIGHTER:
        if skill_types is None or SkillType.WEAPONRY in skill_types:
            result.extend([
                Skill.WAND_AND_DAGGER,
                Skill.SWORD,
                Skill.AXE,
                Skill.MACE_AND_FLAIL,
                Skill.POLE_AND_STAFF,
                Skill.THROWING,
                Skill.SLING,
                Skill.BOWS,
                Skill.SHIELD,
            ])
        if skill_types is None or SkillType.PHYSICAL in skill_types:
            result.extend([
                Skill.SCOUTING,
            ])
        if skill_types is None or SkillType.ACADEMIA in skill_types:
            result.extend([
                Skill.ARTIFACTS,
                Skill.MYTHOLOGY,
                Skill.SCRIBE,
            ])

    else:
        raise RuntimeError(f'Unknown class: {character_class}.')

    return result
