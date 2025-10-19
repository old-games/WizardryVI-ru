# Text Normalization Implementation

## Overview

This document describes the implementation of text normalization for the Wizardry VI Russian translation project. The goal was to preserve the existing Russian translations while restoring the original game markup formatting from the English version.

## Problem

During translation, special control characters and formatting markup from the English text were incorrectly translated or lost in the Russian version. This occurred because:

1. The game uses a custom encoding (OGR001) where certain ASCII control characters map to Cyrillic letters in CP866 encoding
2. For example, `^` (ASCII 94) maps to `Б` (CP866 129) in the OGR001 table
3. When translators saw `Б` in the encoded text, they treated it as the Cyrillic letter and kept it in the translation, losing the original control character

## Solution

Created `tools/normalize_texts.py` which:

1. Identifies format/control characters in English messages:
   - Control characters (ASCII < 32)
   - Special markup: `^`, `%`, `@`, `]`, `!`, `~`

2. Detects mistranslated format characters in Russian:
   - Uses the OGR001 encoding table to identify Cyrillic letters that are mistranslations
   - For example, Cyrillic `Б` at the start of a message where English has `^`

3. Normalizes Russian text by:
   - Replacing mistranslated format characters with the original English format characters
   - Inserting missing format characters when they were completely lost
   - Preserving the actual Russian translation text

## Key Features

### Conservative Approach

The normalization is conservative to avoid damaging valid Russian text:

- Only replaces characters that are clearly mistranslations (e.g., Cyrillic `Б` for `^`)
- Only replaces existing format characters (e.g., `@` for `%%]`)
- Only replaces control characters (like `\x16` for `^`)
- Inserts missing format characters when the Russian text starts with regular text but English has format prefix

### Position-Based Matching

- **Leading format characters**: Processed from the beginning of the message
- **Trailing format characters**: Processed from the end of the message
- **Embedded format characters**: Use context (spaces, underscores) to find corresponding positions

## Results

- **985 messages normalized** out of 5165 total messages (19%)
- All existing tests pass
- Build succeeds with normalized texts
- Created comprehensive test suite with 7 tests covering various normalization scenarios

## Example Transformations

| English | Russian Before | Russian After |
|---------|----------------|---------------|
| `^PERSONAL SPELLBOOK.` | `БКНИГУ ЗАКЛИНАНИЙ.` | `^КНИГУ ЗАКЛИНАНИЙ.` |
| `^ ATTACKS!` | `Б АТАКУЕТ!` | `^ АТАКУЕТ!` |
| `^_no_one_available_^` | `\x16_нет_доступных_\x16` | `^_нет_доступных_^` |
| `%%]SUDDENLY A DOOR...` | `@ВНЕЗАПНО СПРАВА...` | `%%]ВНЕЗАПНО СПРАВА...` |

## Usage

To run the normalization script:

```bash
# Dry run (shows changes without writing)
python3 tools/normalize_texts.py messages/messages.json -d

# Apply normalization
python3 tools/normalize_texts.py messages/messages.json
```

## Testing

Run the normalization tests:

```bash
python3 -m unittest tests.test_normalize_texts -v
```

## Technical Details

### OGR001 Encoding

The OGR001 encoding is a custom encoding used by the game that maps certain ASCII characters to CP866 (Cyrillic) code points. Key mappings relevant to this normalization:

- `^` (ASCII 94) → CP866 129 → Cyrillic `Б`
- Various control characters → Cyrillic letters

This encoding is defined in `tools/text.py` and is used for displaying Russian text in the game. Some letters have two corresponding codes in the OGR001 table - the duplicates are likely used for editable Cyrillic texts (e.g., character names that players can input).

**Note on Future Encodings:**

The project may need a second encoding (OGR002) in the future to properly support all use cases:
- OGR001 for display text (Russian translation)
- OGR002 for editable text (player-entered text like character names)

This separation would allow proper handling of both display and input scenarios with Cyrillic characters.

### Format Characters

The following characters are considered format/markup characters:
- **Control characters**: ASCII < 32 (e.g., `\x01` through `\x1F`)
- **DEL character**: ASCII 127 (`\u007f`) - Used as a special markup character in the game
- **Special symbols**: `^`, `%`, `@`, `]`, `!`, `~`

These characters have special meaning in the game engine and must be preserved exactly as they appear in the English version.

#### Character Meanings

**Primary Markup Characters:**
- `^` (ASCII 94) - Character name placeholder (replaced with character's name during gameplay)
- `%` (ASCII 37) - Event/special formatting prefix (often appears as `%%`, `%%%`)
- `]` (ASCII 93) - Part of event markup (appears after `%` sequences like `%%]`)
- `!` (ASCII 33) - Part of event markup (appears after `%` sequences like `%%!`)
- `@` (ASCII 64) - Alternative formatting character (sometimes mistranslated from `%%]` or other sequences)
- `~` (ASCII 126) - Special formatting character
- `\u007f` (DEL, ASCII 127) - Special markup character used to denote special text sections

**Control Characters (ASCII 0-31):**

The game uses various control characters for formatting, special symbols, and game mechanics. These are displayed as 8x8 pixel character blocks in the game. All control characters are preserved as escape sequences (e.g., `\x01`, `\x15`) rather than Unicode equivalents for easier editing.

Common control characters include:
- `\x01` through `\x05` - Special game symbols and formatting
- `\x06` through `\x08` - Various UI elements
- `\t` (ASCII 9), `\n` (ASCII 10), `\r` (ASCII 13) - Standard whitespace/control
- `\x0B` through `\x0E` - Additional formatting characters
- `\x15` (ASCII 21) - Special symbol (originally considered for ⏎ replacement, kept as-is for editability)
- `\x16` (ASCII 22) - Often appears in mistranslations, replaced with proper format chars
- `\x1E`, `\x1F` (ASCII 30-31) - Common formatting characters

**Game Display System:**

The game outputs text using 8x8 pixel blocks, and all UI elements are constructed from these character blocks. The game only outputs uppercase characters. Some characters have special rendering:
- Characters with underscores (underline) and overscores (overline) for the status line
- Status line appears at the top and bottom of the screen with decorative lines
- "Lowercase" characters in the encoding are used for status line rendering (with decorative lines)

**Font Files:**

Font files are located in `cga/fonts/`, `ega/fonts/`, and `tandy/fonts/` directories. Each character is stored as a separate PNG file named after its code point (e.g., `WFONT0.CGA.127.png` for character 127). There are 5 different fonts used throughout the game for different purposes.
