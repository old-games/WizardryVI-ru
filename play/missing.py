import definition


spells = [
    [
        definition.Spell.ENERGY_BLAST,
        definition.Spell.BLINDING_FLASH,
        definition.Spell.FIREBALL,
        definition.Spell.FIRE_SHIELD,
        definition.Spell.FIRE_BOMB,
        definition.Spell.LIGHTNING,
        definition.Spell.PRISMIC_MISSILE,
        definition.Spell.FIRESTORM,
        definition.Spell.NUCLEAR_BLAST, # FIXME: nuclear blast does not work

        definition.Spell.ACID_SPLASH,
        definition.Spell.ITCHING_SKIN,
        definition.Spell.ARMOR_SHIELD,
        definition.Spell.DIRECTION,
        definition.Spell.KNOCKKNOCK,
        definition.Spell.BLADES,
        definition.Spell.ARMORPLATE,
        definition.Spell.WEB,
        definition.Spell.ACID_BOMB,
        definition.Spell.ARMORMELT,
        definition.Spell.CREATE_LIFE,
        definition.Spell.CURE_STONE,

        definition.Spell.CHILLING_TOUCH,
        definition.Spell.STAMINA,
        definition.Spell.TERROR,
        definition.Spell.WEAKEN,
        definition.Spell.SLOW,
        definition.Spell.HASTE,
        definition.Spell.CURE_PARALYSIS,
        definition.Spell.ICE_SHIELD,
        definition.Spell.ICEBALL,
        definition.Spell.PARALYZE,
        definition.Spell.DEEP_FREEZE,

        definition.Spell.MENTAL_ATTACK,
        definition.Spell.SLEEP,
        definition.Spell.BLESS,
        definition.Spell.CHARM,
        definition.Spell.CURE_LESSER_CND,
        definition.Spell.DIVINE_TRAP,
        definition.Spell.DETECT_SECRET,
        definition.Spell.IDENTIFY,
        definition.Spell.HOLD_MONSTERS,
        definition.Spell.MINDREAD,
        definition.Spell.SANE_MIND,
        definition.Spell.PSIONIC_BLAST,
        definition.Spell.ILLUSION,
        definition.Spell.WIZARD_EYE,
        definition.Spell.DEATH,
        definition.Spell.LOCATE_OBJECT,
        definition.Spell.MIND_FLAY,

        definition.Spell.POISON,
        definition.Spell.MISSILE_SHIELD,
        definition.Spell.STINK_BOMB,
        definition.Spell.AIR_POCKET,
        definition.Spell.SILENCE,
        definition.Spell.POISON_GAS,
        definition.Spell.CURE_POISON,
        definition.Spell.WHIRLWIND,
        definition.Spell.PURIFY_AIR,
        definition.Spell.DEADLY_POISON,
        definition.Spell.LEVITATE,
        definition.Spell.TOXIC_VAPORS,
        definition.Spell.NOXIOUS_FUMES,
        definition.Spell.ASPHYXIATION,
        definition.Spell.DEADLY_AIR,

        definition.Spell.HEAL_WOUNDS,
        definition.Spell.MAKE_WOUNDS,
        definition.Spell.MAGIC_MISSILE,
        definition.Spell.DISPEL_UNDEAD,
        definition.Spell.ENCHANTED_BLADE,
        definition.Spell.BLINK,
        definition.Spell.MAGIC_SCREEN,
        definition.Spell.CONJURATION,
        definition.Spell.ANTIMAGIC,
        definition.Spell.REMOVE_CURSE,
        definition.Spell.LIFESTEAL,
        definition.Spell.ASTRAL_GATE,
        definition.Spell.WORD_OF_DEATH,
        definition.Spell.RESURRECTION,
        definition.Spell.DEATH_WISH,
    ],
    [
        definition.Spell.ENERGY_BLAST,
        definition.Spell.BLINDING_FLASH,
        definition.Spell.FIREBALL,
        definition.Spell.FIRE_SHIELD,
        definition.Spell.FIRE_BOMB,
        definition.Spell.LIGHTNING,
        definition.Spell.PRISMIC_MISSILE,
        definition.Spell.FIRESTORM,
        definition.Spell.NUCLEAR_BLAST, # FIXME: nuclear blast does not work

        definition.Spell.ACID_SPLASH,
        definition.Spell.ITCHING_SKIN,
        definition.Spell.ARMOR_SHIELD,
        definition.Spell.DIRECTION,
        definition.Spell.KNOCKKNOCK,
        definition.Spell.BLADES,
        definition.Spell.ARMORPLATE,
        definition.Spell.WEB,
        definition.Spell.ACID_BOMB,
        definition.Spell.ARMORMELT,
        definition.Spell.CREATE_LIFE,
        definition.Spell.CURE_STONE,

        definition.Spell.CHILLING_TOUCH,
        definition.Spell.STAMINA,
        definition.Spell.TERROR,
        definition.Spell.WEAKEN,
        definition.Spell.SLOW,
        definition.Spell.HASTE,
        definition.Spell.CURE_PARALYSIS,
        definition.Spell.ICE_SHIELD,
        definition.Spell.ICEBALL,
        definition.Spell.PARALYZE,
        definition.Spell.DEEP_FREEZE,

        definition.Spell.MENTAL_ATTACK,
        definition.Spell.SLEEP,
        definition.Spell.BLESS,
        definition.Spell.CHARM,
        definition.Spell.CURE_LESSER_CND,
        definition.Spell.DIVINE_TRAP,
        definition.Spell.DETECT_SECRET,
        definition.Spell.IDENTIFY,
        definition.Spell.HOLD_MONSTERS,
        definition.Spell.MINDREAD,
        definition.Spell.SANE_MIND,
        definition.Spell.PSIONIC_BLAST,
        definition.Spell.ILLUSION,
        definition.Spell.WIZARD_EYE,
        definition.Spell.DEATH,
        definition.Spell.LOCATE_OBJECT,
        definition.Spell.MIND_FLAY,

        definition.Spell.POISON,
        definition.Spell.MISSILE_SHIELD,
        definition.Spell.STINK_BOMB,
        definition.Spell.AIR_POCKET,
        definition.Spell.SILENCE,
        definition.Spell.POISON_GAS,
        definition.Spell.CURE_POISON,
        definition.Spell.WHIRLWIND,
        definition.Spell.PURIFY_AIR,
        definition.Spell.DEADLY_POISON,
        definition.Spell.LEVITATE,
        definition.Spell.TOXIC_VAPORS,
        definition.Spell.NOXIOUS_FUMES,
        definition.Spell.ASPHYXIATION,
        definition.Spell.DEADLY_AIR,

        definition.Spell.HEAL_WOUNDS,
        definition.Spell.MAKE_WOUNDS,
        definition.Spell.MAGIC_MISSILE,
        definition.Spell.DISPEL_UNDEAD,
        definition.Spell.ENCHANTED_BLADE,
        definition.Spell.BLINK,
        definition.Spell.MAGIC_SCREEN,
        definition.Spell.CONJURATION,
        definition.Spell.ANTIMAGIC,
        definition.Spell.REMOVE_CURSE,
        definition.Spell.LIFESTEAL,
        definition.Spell.ASTRAL_GATE,
        definition.Spell.WORD_OF_DEATH,
        definition.Spell.RESURRECTION,
        definition.Spell.DEATH_WISH,
    ],
]
skills = [
    [],
    [],
]


def spellbook_for_spell(spell):
    """Return a list of Spellbooks that contain the given spell."""
    result = []
    for spellbook in definition.Spellbook:
        spells = definition.get_spellbook_spells(spellbook)
        if spell in spells:
            result.append(spellbook)
    return result


def missing_spells_report(char_spells):
    all_spells = set()
    for spellbook in definition.Spellbook:
        all_spells.update(definition.get_spellbook_spells(spellbook))

    for idx, known_spells in enumerate(char_spells):
        known_set = set(known_spells)
        missing = sorted(all_spells - known_set, key=lambda s: s.name)
        print(f"Character {idx+1}:")
        for spell in missing:
            books = spellbook_for_spell(spell)
            books_str = ', '.join(b.name for b in books)
            print(f"  Missing: {spell.name} (in: {books_str})")
        print()


def unique_and_unassigned_spells_report():
    # Map each spell to the set of spellbooks it belongs to
    spell_to_books = {}
    all_spells = set()
    for spellbook in definition.Spellbook:
        spells = definition.get_spellbook_spells(spellbook)
        for spell in spells:
            all_spells.add(spell)
            spell_to_books.setdefault(spell, set()).add(spellbook)
    # Find all spells defined in Spell enum
    all_defined_spells = set(definition.Spell)
    # Spells not in any spellbook
    unassigned_spells = sorted(all_defined_spells - all_spells, key=lambda s: s.name)
    if unassigned_spells:
        print("Spells not present in any spellbook:")
        for spell in unassigned_spells:
            print(f"  {spell.name}")
        print()
    # Spells unique to each spellbook
    for spellbook in definition.Spellbook:
        spells = set(definition.get_spellbook_spells(spellbook))
        unique_spells = [spell for spell in spells if len(spell_to_books.get(spell, [])) == 1]
        if unique_spells:
            print(f"Spells only in {spellbook.name}:")
            for spell in sorted(unique_spells, key=lambda s: s.name):
                print(f"  {spell.name}")
            print()


if __name__ == "__main__":
    missing_spells_report(spells)
    unique_and_unassigned_spells_report()
