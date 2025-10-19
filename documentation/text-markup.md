# Text Markup and Special Characters

This document describes the special characters and markup used in Wizardry VI game text.

## Overview

The game uses custom markup characters to control text display, insert dynamic content, and format the UI. All text is rendered using 8x8 pixel character blocks, and the entire UI is constructed from these blocks.

## Markup Characters

### Character Name Placeholder

**`^` (ASCII 94)**
- Replaced with a character's name during gameplay
- Example: `"^ ATTACKS!"` becomes `"GANDALF ATTACKS!"` when Gandalf attacks

### Event and Special Formatting

**`%` (ASCII 37)**
- Event/special formatting prefix
- Often appears as sequences: `%%`, `%%%`
- Used in combination with other characters for special effects

**`]` (ASCII 93)**
- Part of event markup when following `%` sequences
- Example: `%%]SUDDENLY THE DOOR SLAMS SHUT!`

**`!` (ASCII 33)**
- Part of event markup when following `%` sequences  
- Example: `%%!YOU ARE BEING WATCHED...`

**`@` (ASCII 64)**
- Alternative formatting character
- Sometimes appears in place of multi-character sequences

**`~` (ASCII 126)**
- Special formatting character

**`\u007f` (DEL, ASCII 127)**
- Special markup character denoting special text sections
- Example: `"\u007f__master_options__\u007f"` for emphasized menu options

## Control Characters

The game uses various control characters (ASCII 0-31) for formatting, special symbols, and game mechanics. These characters are stored as escape sequences in the JSON files (e.g., `\u0001`, `\u0015`) for readability and editability.

### Common Control Characters

- `\u0001` through `\u0005` - Special game symbols and formatting
- `\u0006` through `\u0008` - Various UI elements
- `\t` (ASCII 9), `\n` (ASCII 10), `\r` (ASCII 13) - Standard whitespace/control characters
- `\u000b` through `\u000e` - Additional formatting characters
- `\u0015` (ASCII 21) - Special symbol (could represent ⏎ visually, but stored as escape for editability)
- `\u0016` (ASCII 22), `\u0017` (ASCII 23) - Formatting characters
- `\u001e`, `\u001f` (ASCII 30-31) - Common formatting characters

## Game Display System

### Character Rendering

- All text is rendered using **8x8 pixel blocks**
- The game **only outputs uppercase** characters
- Font files are located in `cga/fonts/`, `ega/fonts/`, and `tandy/fonts/`
- Each character is stored as a PNG file named after its code point (e.g., `WFONT0.CGA.127.png` for character 127)
- There are 5 different fonts used throughout the game

### Status Line

- Status lines appear at the **top and bottom** of the screen
- Status lines have decorative horizontal lines
- Characters in status lines use special rendering with:
  - **Underscores** (underline) 
  - **Overscores** (overline)
- "Lowercase" character codes in the encoding map to status line versions with decorative lines
- Regular text uses uppercase codes, status line text uses lowercase codes

## Text Encoding

### OGR001 Encoding

The game uses a custom OGR001 encoding that maps ASCII characters to CP866 (Cyrillic) code points for Russian text display.

**Key mappings:**
- `^` (ASCII 94) → CP866 129 → Cyrillic `Б`
- Various control characters → Cyrillic letters

The OGR001 table is defined in `tools/text.py`. Some Cyrillic letters have two corresponding codes - the duplicates are used for editable text (e.g., player-entered character names).

### Future: OGR002 Encoding

A second encoding (OGR002) may be needed to properly support all use cases:
- **OGR001** for display text (Russian translation of game messages)
- **OGR002** for editable text (player input like character names)

This separation would allow proper handling of both display and input scenarios with Cyrillic characters.

## File Format

### JSON Representation

Text is stored in JSON files (e.g., `messages/messages.json`) with:
- **Escape sequences** for control characters: `\u0001`, `\u007f`, etc.
- **Cyrillic text** in UTF-8 encoding
- **4-space indentation** for readability
- Control characters appear as `\uXXXX` (not actual bytes) for visibility and editability

Example:
```json
{
    "01001": {
        "en": "\u007f__master_options__\u007f",
        "ru": "\u007f__главное_меню__\u007f"
    },
    "00721": {
        "en": "^PERSONAL SPELLBOOK.",
        "ru": "^КНИГУ ЗАКЛИНАНИЙ."
    }
}
```

### Why Escape Sequences?

Control characters are stored as escape sequences (like `\u0015`) rather than Unicode visual equivalents (like ⏎) because:
- **Easier to edit** - escape sequences are simple text
- **No confusion** - clear distinction between game characters and Unicode symbols
- **Compatible** - works in any text editor
- **Maintainable** - no need for special editor support

## Translation Guidelines

When translating game text:

1. **Preserve all markup characters exactly** - Copy `^`, `%`, `@`, `]`, `!`, `~`, `\u007f`, and all control characters from English
2. **Translate only the text content** - Don't translate markup or control characters
3. **Maintain character positions** - Markup at start/end of English should be at start/end of Russian
4. **Keep escape sequences** - Don't convert `\uXXXX` to actual characters or Unicode symbols

Example:
```
EN: "^PERSONAL SPELLBOOK."
RU: "^КНИГУ ЗАКЛИНАНИЙ."     ✓ Correct - ^ preserved
RU: "БКНИГУ ЗАКЛИНАНИЙ."     ✗ Wrong - ^ became Б
```

## Tools

### Normalization Script

The `tools/normalize_texts.py` script ensures Russian translations preserve the original markup:
- Detects mistranslated format characters (e.g., `Б` instead of `^`)
- Restores correct markup from English source
- Preserves all Russian translation text
- Outputs properly escaped JSON

This is a **one-time import tool** used when importing translations from external sources.

### Encoding/Decoding

The `tools/text.py` module provides:
- `encode()` - Convert text to game format using OGR001 encoding
- `decode()` - Convert game data back to text
- Character mapping tables for display and editing
