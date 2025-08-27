import definition


spells = [
    [
        definition.Spell.KNOCKKNOCK,

        definition.Spell.STAMINA,
        definition.Spell.TERROR,
        definition.Spell.WEAKEN,
        definition.Spell.SLOW,

        definition.Spell.MENTAL_ATTACK,
        definition.Spell.SLEEP,
        definition.Spell.BLESS,
        definition.Spell.CHARM,
        definition.Spell.CURE_LESSER_CND,
        definition.Spell.DIVINE_TRAP,
        definition.Spell.DETECT_SECRET,
        definition.Spell.IDENTIFY,

        definition.Spell.HEAL_WOUNDS,
    ],
    [
        definition.Spell.ENERGY_BLAST,

        definition.Spell.ARMOR_SHIELD,
        definition.Spell.DIRECTION,
        definition.Spell.BLADES,
        definition.Spell.ARMORPLATE,

        definition.Spell.CHILLING_TOUCH,
        definition.Spell.STAMINA,
        definition.Spell.TERROR,
        definition.Spell.SLOW,
        definition.Spell.HASTE,
        definition.Spell.CURE_PARALYSIS,

        definition.Spell.SLEEP,
        definition.Spell.BLESS,
        definition.Spell.CHARM,
        definition.Spell.CURE_LESSER_CND,
        definition.Spell.DIVINE_TRAP,
        definition.Spell.IDENTIFY,
        definition.Spell.HOLD_MONSTERS,
        definition.Spell.SANE_MIND,

        definition.Spell.MISSILE_SHIELD,
        definition.Spell.SILENCE,

        definition.Spell.HEAL_WOUNDS,
        definition.Spell.MAKE_WOUNDS,
        definition.Spell.MAGIC_MISSILE,
        definition.Spell.DISPEL_UNDEAD,
        definition.Spell.ENCHANTED_BLADE,
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


if __name__ == "__main__":
    missing_spells_report(spells)
