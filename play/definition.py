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
    PSIONIC = enum.auto()
    PRIEST = enum.auto()
    MAGE = enum.auto()
    ALCHEMIST = enum.auto()


class Spell(enum.Enum):
    # Fire:
    ENERGY_BLAST = enum.auto()
    BLINDING_FLASH = enum.auto()
    FIREBALL = enum.auto()
    FIRE_SHIELD = enum.auto()
    FIRE_BOMB = enum.auto()
    LIGHTNING = enum.auto()
    PRISMIC_MISSILE = enum.auto()
    FIRESTORM = enum.auto()
    NUCLEAR_BLAST = enum.auto()

    # Water:
    CHILLING_TOUCH = enum.auto()
    STAMINA = enum.auto()
    TERROR = enum.auto()
    WEAKEN = enum.auto()
    SLOW = enum.auto()
    HASTE = enum.auto()
    CURE_PARALYSIS = enum.auto()
    ICE_SHIELD = enum.auto()
    ICEBALL = enum.auto()
    PARALYZE = enum.auto()
    DEEP_FREEZE = enum.auto()

    # Air:
    POISON = enum.auto()
    MISSILE_SHIELD = enum.auto()
    STINK_BOMB = enum.auto()
    AIR_POCKET = enum.auto()
    SILENCE = enum.auto()
    POISON_GAS = enum.auto()
    CURE_POISON = enum.auto()
    WHIRLWIND = enum.auto()
    PURIFY_AIR = enum.auto()
    DEADLY_POISON = enum.auto()
    LEVITATE = enum.auto()
    TOXIC_VAPORS = enum.auto()
    NOXIOUS_FUMES = enum.auto()
    ASPHYXIATION = enum.auto()
    DEADLY_AIR = enum.auto()

    # Earth:
    ACID_SPLASH = enum.auto()
    ITCHING_SKIN = enum.auto()
    ARMOR_SHIELD = enum.auto()
    DIRECTION = enum.auto()
    KNOCKKNOCK = enum.auto()
    BLADES = enum.auto()
    ARMORPLATE = enum.auto()
    WEB = enum.auto()
    ACID_BOMB = enum.auto()
    ARMORMELT = enum.auto()
    CREATE_LIFE = enum.auto()
    CURE_STONE = enum.auto()

    # Mental:
    MENTAL_ATTACK = enum.auto()
    SLEEP = enum.auto()
    BLESS = enum.auto()
    CHARM = enum.auto()
    CURE_LESSER_CND = enum.auto()
    DIVINE_TRAP = enum.auto()
    DETECT_SECRET = enum.auto()
    IDENTIFY = enum.auto()
    HOLD_MONSTERS = enum.auto()
    MINDREAD = enum.auto()
    SANE_MIND = enum.auto()
    PSIONIC_BLAST = enum.auto()
    ILLUSION = enum.auto()
    WIZARD_EYE = enum.auto()
    DEATH = enum.auto()
    LOCATE_OBJECT = enum.auto()
    MIND_FLAY = enum.auto()

    # Magic:
    HEAL_WOUNDS = enum.auto()
    MAKE_WOUNDS = enum.auto()
    MAGIC_MISSILE = enum.auto()
    DISPEL_UNDEAD = enum.auto()
    ENCHANTED_BLADE = enum.auto()
    BLINK = enum.auto()
    MAGIC_SCREEN = enum.auto()
    CONJURATION = enum.auto()
    ANTIMAGIC = enum.auto()
    REMOVE_CURSE = enum.auto()
    LIFESTEAL = enum.auto()
    ASTRAL_GATE = enum.auto()
    WORD_OF_DEATH = enum.auto()
    RESURRECTION = enum.auto()
    DEATH_WISH = enum.auto()

    # Special:
    HOLY_WATER = enum.auto()
    HELPFOOD = enum.auto()
    MAGICFOOD = enum.auto()


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
    SWIMMING = enum.auto() # Hidden.
    SCOUTING = enum.auto()
    MUSIC = enum.auto()
    ORATORY = enum.auto()
    LEGERDEMAIN = enum.auto()
    SKULDUGGERY = enum.auto()
    NINJUTSU = enum.auto()

    # Personal:
    DEFENSE = enum.auto()
    SPEED = enum.auto()
    MOVEMENT = enum.auto()
    AIM = enum.auto()
    POWER = enum.auto()

    # Academia:
    ARTIFACTS = enum.auto()
    MYTHOLOGY = enum.auto()
    SCRIBE = enum.auto()
    ALCHEMY = enum.auto()
    THEOLOGY = enum.auto()
    THEOSOPHY = enum.auto()
    THAUMATURGY = enum.auto()
    KIRIJUTSU = enum.auto()


POINTS_PROBABILITIES = {
    Race.HUMAN: [(7, 68), (5, 60), (8, 59), (10, 58), (6, 54), (9, 53), (17, 11), (14, 9), (15, 8), (18, 6), (13, 5), (16, 5)],
    Race.LIZARDMAN: [(5, 69), (7, 66), (9, 66), (6, 65), (8, 62), (10, 54), (16, 11), (14, 9), (13, 8), (17, 6), (15, 4), (18, 4), (22, 1)],
}


__LEVEL_EXPERIENCES = { #   1     2     3     4      5      6      7      8       9      10      11       12       13       14       15
    Class.FIGHTER:   [None, 0, 1000, 2000, 4000,  8000, 16000, 32000, 64000, 128000, 256000, 512000,  768000, 1024000, 1280000, 1536000],
    Class.MAGE:      [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1015000, 1390000, 1760000, 2130000],
    Class.PRIEST:    [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1015000, 1390000, 1760000, 2130000],
    Class.THIEF:     [None, 0,  900, 1800, 3600,  7200, 14400, 28800, 57600, 115200, 230400, 460800,  685800,  910800, 1138800, 1366800],
    Class.RANGER:    [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800, 1131800, 1546800, 1961800, 2376800],
    Class.ALCHEMIST: [None, 0, 1100, 2200, 4400,  8800, 17600, 35200, 70400, 140800, 281600, 563200,  875200, 1187200, 1499200, 1811200],
    Class.BARD:      [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1015000, 1390000, 1760000, 2130000],
    Class.PSIONIC:   [None, 0, 1250, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1015000, 1390000, 1760000, 2130000],
    Class.VALKYRIE:  [None, 0, 1100, 2200, 4400,  8800, 17600, 35200, 70400, 140800, 281600, 563200,  875200, 1187200, 1499200, 1811200],
    Class.BISHOP:    [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000, 1213000, 1658000, 2103000, 2548000],
    Class.SAMURAI:   [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800, 1131800, 1546800, 1961800, 2376800],
    Class.MONK:      [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800, 1131800, 1546800, 1961800, 2376800],
    Class.NINJA:     [None, 0, 1500, 3000, 6000, 12000, 24000, 48000, 96000, 192000, 384000, 768000, 1243000, 1718000, 2193000, 2668000],
    Class.LORD:      [None, 0, 1400, 2800, 5600, 11200, 22400, 44800, 89600, 179200, 358400, 716800, 1131800, 1546800, 1961800, 2376800],
}


def get_level_experience(character_class: Class, level: int):
    if level < 1 or not isinstance(level, int):
        raise RuntimeError(f'Invalid level: {level}.')

    else:
        class_experiences = __LEVEL_EXPERIENCES[character_class]
        if level < len(class_experiences):
            return class_experiences[level]

        else:
            return class_experiences[-1] + (level - (len(class_experiences) - 1)) * (class_experiences[-1] - class_experiences[-2])


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
        return {                        Parameter.INTELLIGENCE: 12}
    elif character_class == Class.PRIEST:
        return {                                                    Parameter.PIETY: 12,                                                                       Parameter.PERSONALITY:  8}
    elif character_class == Class.THIEF:
        return {                                                                                                 Parameter.DEXTERITY: 12, Parameter.SPEED:  8}
    elif character_class == Class.RANGER:
        return {Parameter.STRENGTH: 10, Parameter.INTELLIGENCE:  8, Parameter.PIETY:  8, Parameter.VITALITY: 11, Parameter.DEXTERITY: 10, Parameter.SPEED:  8, Parameter.PERSONALITY:  8}
    elif character_class == Class.ALCHEMIST:
        return {                        Parameter.INTELLIGENCE: 13,                                              Parameter.DEXTERITY: 13}
    elif character_class == Class.BARD:
        return {                        Parameter.INTELLIGENCE: 10,                                              Parameter.DEXTERITY: 12, Parameter.SPEED:  8, Parameter.PERSONALITY: 12}
    elif character_class == Class.PSIONIC:
        return {Parameter.STRENGTH: 10, Parameter.INTELLIGENCE: 14,                      Parameter.VITALITY: 14,                                               Parameter.PERSONALITY: 10}
    elif character_class == Class.VALKYRIE:
        return {Parameter.STRENGTH: 10,                             Parameter.PIETY: 11, Parameter.VITALITY: 11, Parameter.DEXTERITY: 10, Parameter.SPEED: 11, Parameter.PERSONALITY:  8}
    elif character_class == Class.BISHOP:
        return {                        Parameter.INTELLIGENCE: 15, Parameter.PIETY: 15,                                                                       Parameter.PERSONALITY:  8}
    elif character_class == Class.LORD:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE:  9, Parameter.PIETY: 12, Parameter.VITALITY: 12, Parameter.DEXTERITY:  9, Parameter.SPEED:  9, Parameter.PERSONALITY: 14}
    elif character_class == Class.SAMURAI:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE: 11,                      Parameter.VITALITY:  9, Parameter.DEXTERITY: 12, Parameter.SPEED: 14, Parameter.PERSONALITY:  8}
    elif character_class == Class.MONK:
        return {Parameter.STRENGTH: 13, Parameter.INTELLIGENCE:  8, Parameter.PIETY: 13,                         Parameter.DEXTERITY: 10, Parameter.SPEED: 13, Parameter.PERSONALITY:  8}
    elif character_class == Class.NINJA:
        return {Parameter.STRENGTH: 12, Parameter.INTELLIGENCE: 10, Parameter.PIETY: 10, Parameter.VITALITY: 12, Parameter.DEXTERITY: 12, Parameter.SPEED: 12}
    else:
        raise RuntimeError(f'Unknown class: {character_class}.')


def get_class_spellbooks(character_class: Class) -> list[Spellbook]:
    if character_class in (Class.MAGE, Class.BARD, Class.SAMURAI):
        return [Spellbook.MAGE]
    elif character_class in (Class.PRIEST, Class.VALKYRIE, Class.LORD):
        return [Spellbook.PRIEST]
    elif character_class in (Class.ALCHEMIST, Class.RANGER, Class.NINJA):
        return [Spellbook.ALCHEMIST]
    elif character_class in (Class.PSIONIC, Class.MONK):
        return [Spellbook.PSIONIC]
    elif character_class == Class.BISHOP:
        return [Spellbook.MAGE, Spellbook.PRIEST]
    else:
        return []


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


def get_spellbook_spells(spellbook: Spellbook) -> list[Spell]:
    if spellbook == Spellbook.MAGE:
        return [
            Spell.ENERGY_BLAST,
            Spell.FIREBALL,
            Spell.FIRE_SHIELD,
            Spell.PRISMIC_MISSILE,
            Spell.FIRESTORM,
            Spell.NUCLEAR_BLAST,

            Spell.CHILLING_TOUCH,
            Spell.TERROR,
            Spell.WEAKEN,
            Spell.ICE_SHIELD,
            Spell.ICEBALL,
            Spell.DEEP_FREEZE,

            Spell.MISSILE_SHIELD,
            Spell.STINK_BOMB,
            Spell.AIR_POCKET,
            Spell.LEVITATE,
            Spell.NOXIOUS_FUMES,
            Spell.ASPHYXIATION,

            Spell.ARMOR_SHIELD,
            Spell.DIRECTION,
            Spell.KNOCKKNOCK,
            Spell.WEB,
            Spell.ARMORMELT,

            Spell.SLEEP,
            Spell.DETECT_SECRET,
            Spell.WIZARD_EYE,

            Spell.MAGIC_MISSILE,
            Spell.BLINK,
            Spell.MAGIC_SCREEN,
            Spell.CONJURATION,
            Spell.ANTIMAGIC,
            Spell.ASTRAL_GATE,
            Spell.RESURRECTION,
        ]

    elif spellbook == Spellbook.PRIEST:
        return [
            Spell.LIGHTNING,

            Spell.STAMINA,
            Spell.SLOW,
            Spell.HASTE,
            Spell.CURE_PARALYSIS,
            Spell.PARALYZE,

            Spell.SILENCE,
            Spell.CURE_POISON,
            Spell.WHIRLWIND,
            Spell.PURIFY_AIR,

            Spell.ARMORPLATE,
            Spell.BLADES,
            Spell.CURE_STONE,

            Spell.BLESS,
            Spell.CHARM,
            Spell.CURE_LESSER_CND,
            Spell.DIVINE_TRAP,
            Spell.IDENTIFY,
            Spell.HOLD_MONSTERS,
            Spell.SANE_MIND,
            Spell.DEATH,
            Spell.LOCATE_OBJECT,

            Spell.HEAL_WOUNDS,
            Spell.MAKE_WOUNDS,
            Spell.DISPEL_UNDEAD,
            Spell.ENCHANTED_BLADE,
            Spell.CONJURATION,
            Spell.REMOVE_CURSE,
            Spell.LIFESTEAL,
            Spell.ASTRAL_GATE,
            Spell.WORD_OF_DEATH,
            Spell.RESURRECTION,
            Spell.DEATH_WISH,
        ]

    elif spellbook == Spellbook.ALCHEMIST:
        return [
            Spell.BLINDING_FLASH,
            Spell.FIRE_BOMB,

            Spell.STAMINA,
            Spell.CURE_PARALYSIS,

            Spell.POISON,
            Spell.STINK_BOMB,
            Spell.AIR_POCKET,
            Spell.POISON_GAS,
            Spell.CURE_POISON,
            Spell.DEADLY_POISON,
            Spell.PURIFY_AIR,
            Spell.TOXIC_VAPORS,
            Spell.NOXIOUS_FUMES,
            Spell.ASPHYXIATION,
            Spell.DEADLY_AIR,

            Spell.ACID_SPLASH,
            Spell.ITCHING_SKIN,
            Spell.WEB,
            Spell.ACID_BOMB,
            Spell.CREATE_LIFE,
            Spell.CURE_STONE,

            Spell.SLEEP,
            Spell.CHARM,
            Spell.CURE_LESSER_CND,

            Spell.HEAL_WOUNDS,
        ]

    elif spellbook == Spellbook.PSIONIC:
        return [
            Spell.STAMINA,
            Spell.TERROR,
            Spell.WEAKEN,
            Spell.SLOW,
            Spell.HASTE,
            Spell.CURE_PARALYSIS,
            Spell.PARALYZE,

            Spell.SILENCE,

            Spell.KNOCKKNOCK,
            Spell.BLADES,
            Spell.ARMORMELT,

            Spell.MENTAL_ATTACK,
            Spell.SLEEP,
            Spell.BLESS,
            Spell.CHARM,
            Spell.CURE_LESSER_CND,
            Spell.DIVINE_TRAP,
            Spell.DETECT_SECRET,
            Spell.IDENTIFY,
            Spell.HOLD_MONSTERS,
            Spell.MINDREAD,
            Spell.SANE_MIND,
            Spell.PSIONIC_BLAST,
            Spell.ILLUSION,
            Spell.WIZARD_EYE,
            Spell.DEATH,
            Spell.LOCATE_OBJECT,
            Spell.MIND_FLAY,

            Spell.HEAL_WOUNDS,
            Spell.BLINK,
            Spell.LIFESTEAL,
            Spell.RESURRECTION,
        ]

    else:
        raise RuntimeError(f'Unknown spellbook: {spellbook}.')
