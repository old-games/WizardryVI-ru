#!/usr/bin/env python3
"""
Normalize Russian translations to preserve original game markup from English.

This script fixes the issue where special control characters and formatting
from the English text were lost or incorrectly translated in the Russian version.
It preserves the actual translated text while restoring the original formatting.
"""

import json
import sys
from tools.text import OGR001


def get_format_positions(text):
    """
    Extract positions and types of all formatting/control characters.
    Returns a list of (position, character) tuples.
    """
    positions = []
    for i, char in enumerate(text):
        byte_val = ord(char)
        # Special characters that are formatting/control:
        # - Control characters (< 32)
        # - ^ (94) - character name placeholder
        # - % (37) - special formatting
        # - @ (64) - special formatting
        # - ~ (126) - special formatting
        if byte_val < 32 or byte_val in [37, 64, 94, 126]:
            positions.append((i, char))
    return positions


def normalize_text(en_text, ru_text):
    """
    Normalize Russian text to have the same formatting as English.
    
    This preserves the Russian translation but replaces formatting characters
    that were incorrectly translated with the original English formatting.
    
    Strategy:
    1. Find all formatting positions in English text
    2. Build a new Russian text by:
       - Copying formatting characters from English at the same positions
       - Keeping Russian text content, adjusting for length differences
    """
    if not en_text or not ru_text:
        return ru_text
    
    # Get formatting from English
    en_format = get_format_positions(en_text)
    
    if not en_format:
        # No formatting in English, return Russian as-is
        return ru_text
    
    # For texts starting with formatting, we try to preserve it
    result = list(ru_text)
    
    # Check if English starts with formatting character(s)
    if en_format and en_format[0][0] == 0:
        # English starts with formatting
        start_format = []
        for pos, char in en_format:
            if pos < 10:  # Only check first few characters
                start_format.append((pos, char))
            else:
                break
        
        # Check if Russian has a different character at those positions
        # If it does, it might be a mistranslation of the formatting
        for pos, char in start_format:
            if pos < len(result):
                ru_char = result[pos]
                # Check if this Russian character is a Cyrillic letter that
                # might be a mistranslation of the control character
                if char == '^' and ru_char == 'Б':
                    result[pos] = char
                elif char == '^' and ord(ru_char) >= 128:
                    # Any Cyrillic at position where ^ should be
                    result[pos] = char
                elif char in ['%', '@'] and ru_char in ['%', '@', 'Б']:
                    result[pos] = char
                elif ord(char) < 32:
                    # Control character - preserve it
                    result[pos] = char
    
    # Also handle formatting at the end
    if en_format and en_text.endswith(en_format[-1][1]):
        end_char = en_format[-1][1]
        if len(result) > 0 and result[-1] != end_char:
            # Check if last char is a mistranslation
            if end_char == '^' and result[-1] in ['Б', '\x16']:
                result[-1] = end_char
    
    return ''.join(result)


def normalize_messages(input_file, output_file=None):
    """
    Normalize all messages in the JSON file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    normalized_count = 0
    for key, val in data.items():
        en = val.get('en', '') or ''
        ru = val.get('ru', '') or ''
        
        if en and ru:
            new_ru = normalize_text(en, ru)
            if new_ru != ru:
                data[key]['ru'] = new_ru
                normalized_count += 1
    
    print(f"Normalized {normalized_count} messages out of {len(data)}")
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        # Print to stdout
        print(json.dumps(data, ensure_ascii=False, indent=4))
    
    return normalized_count


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Normalize Russian translations')
    parser.add_argument('input', help='Input JSON file')
    parser.add_argument('-o', '--output', help='Output JSON file (default: overwrite input)')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Dry run - show changes without writing')
    
    args = parser.parse_args()
    
    output = args.output if not args.dry_run else None
    if output is None and not args.dry_run:
        output = args.input
    
    normalize_messages(args.input, output)
