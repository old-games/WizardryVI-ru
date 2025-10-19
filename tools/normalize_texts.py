#!/usr/bin/env python3
"""
Normalize Russian translations to preserve original game markup from English.

This script fixes the issue where special control characters and formatting
from the English text were lost or incorrectly translated in the Russian version.
It preserves the actual translated text while restoring the original formatting.
"""

import json
import sys
import os

# Add parent directory to path to import tools module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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


def is_format_char(char):
    """Check if a character is a formatting/control character."""
    byte_val = ord(char)
    # Control chars (< 32) or special markup: %, @, ^, ~, ], !
    # ] and ! are part of game markup when they appear after % sequences
    return byte_val < 32 or byte_val in [33, 37, 64, 93, 94, 126]


def could_be_mistranslated_format(char):
    """Check if a character could be a mistranslated format character."""
    # Cyrillic letters that might be mistranslations of format chars
    # Especially Б which is the OGR001 encoding of ^
    if ord(char) >= 128:  # Cyrillic or high ASCII
        return True
    # Also check for other common replacements
    if char in ['%', '@', '\x16', '\x17']:
        return True
    return False


def normalize_text(en_text, ru_text):
    """
    Normalize Russian text to have the same formatting as English.
    
    This preserves the Russian translation but corrects formatting characters
    that were incorrectly translated.
    
    Strategy:
    1. Replace only characters that are definitely mistranslations
    2. Insert missing format characters at the beginning/end
    3. Be conservative to avoid damaging valid Russian text
    """
    if not en_text or not ru_text:
        return ru_text
    
    # Get formatting from English
    en_format = get_format_positions(en_text)
    
    if not en_format:
        # No formatting in English, return Russian as-is
        return ru_text
    
    result = list(ru_text)
    
    # Track which English format positions we've handled
    handled_en_positions = set()
    
    # Handle leading format characters (most common case)
    en_leading = []
    for i, ch in enumerate(en_text):
        if is_format_char(ch):
            en_leading.append(ch)
            handled_en_positions.add(i)
        else:
            break
    
    if en_leading:
        # Be more careful: only replace obvious mistranslations
        # Map OGR001 mistranslations
        from tools.text import OGR001
        
        # Build reverse map: what Cyrillic letters are mistranslations of format chars
        mistranslation_map = {}
        for ascii_code, cp866_code in OGR001.items():
            if ascii_code < 32 or ascii_code in [33, 37, 64, 93, 94, 126]:
                try:
                    cyrillic = bytes([cp866_code]).decode('cp866')
                    mistranslation_map[cyrillic] = chr(ascii_code)
                except:
                    pass
        
        # Now process leading chars
        ru_idx = 0
        for en_ch in en_leading:
            if ru_idx < len(result):
                ru_ch = result[ru_idx]
                
                # Case 1: Already the right format char - keep it
                if ru_ch == en_ch:
                    ru_idx += 1
                    continue
                
                # Case 2: Is a known mistranslation (like Б for ^)
                if ru_ch in mistranslation_map and mistranslation_map[ru_ch] == en_ch:
                    result[ru_idx] = en_ch
                    ru_idx += 1
                    continue
                
                # Case 3: Is another format char (like @ for %)
                if is_format_char(ru_ch):
                    result[ru_idx] = en_ch
                    ru_idx += 1
                    continue
                
                # Case 4: Is some other char (mistranslation artifact like \x16)
                if ord(ru_ch) < 32 or ru_ch in ['\x16', '\x17']:
                    result[ru_idx] = en_ch
                    ru_idx += 1
                    continue
                
                # Case 5: Regular char - insert the format char before it
                result.insert(ru_idx, en_ch)
                ru_idx += 1
            else:
                # Append at end
                result.append(en_ch)
                ru_idx += 1
    
    # Handle trailing format characters
    en_trailing = []
    for i in range(len(en_text) - 1, -1, -1):
        ch = en_text[i]
        if is_format_char(ch) and i not in handled_en_positions:
            en_trailing.insert(0, ch)
            handled_en_positions.add(i)
        else:
            break
    
    if en_trailing:
        # Process from the end
        from tools.text import OGR001
        mistranslation_map = {}
        for ascii_code, cp866_code in OGR001.items():
            if ascii_code < 32 or ascii_code in [33, 37, 64, 93, 94, 126]:
                try:
                    cyrillic = bytes([cp866_code]).decode('cp866')
                    mistranslation_map[cyrillic] = chr(ascii_code)
                except:
                    pass
        
        ru_idx = len(result) - 1
        for en_ch in reversed(en_trailing):
            if ru_idx >= 0:
                ru_ch = result[ru_idx]
                
                if ru_ch == en_ch:
                    ru_idx -= 1
                    continue
                
                if ru_ch in mistranslation_map and mistranslation_map[ru_ch] == en_ch:
                    result[ru_idx] = en_ch
                    ru_idx -= 1
                    continue
                
                if is_format_char(ru_ch):
                    result[ru_idx] = en_ch
                    ru_idx -= 1
                    continue
                
                if ord(ru_ch) < 32 or ru_ch in ['\x16', '\x17']:
                    result[ru_idx] = en_ch
                    ru_idx -= 1
                    continue
                
                # Regular char - insert after it
                result.insert(ru_idx + 1, en_ch)
                # ru_idx stays same
            else:
                result.insert(0, en_ch)
    
    # Handle middle format characters (embedded in text)
    for i, ch in enumerate(en_text):
        if i in handled_en_positions:
            continue
        if not is_format_char(ch):
            continue
        
        # This is a format char in the middle
        # Look at context to find corresponding position
        
        # Check context before
        has_space_before = i > 0 and en_text[i - 1] == ' '
        has_underscore_before = i > 0 and en_text[i - 1] == '_'
        
        # Build mistranslation map
        from tools.text import OGR001
        mistranslation_map = {}
        for ascii_code, cp866_code in OGR001.items():
            if ascii_code < 32 or ascii_code in [33, 37, 64, 93, 94, 126]:
                try:
                    cyrillic = bytes([cp866_code]).decode('cp866')
                    mistranslation_map[cyrillic] = chr(ascii_code)
                except:
                    pass
        
        # Find similar context in Russian
        if has_space_before:
            # Look for first space followed by mistranslation
            for j in range(len(result) - 1):
                if result[j] == ' ' and j + 1 < len(result):
                    next_ch = result[j + 1]
                    if next_ch in mistranslation_map and mistranslation_map[next_ch] == ch:
                        result[j + 1] = ch
                        break
                    elif is_format_char(next_ch) or ord(next_ch) < 32 or next_ch in ['\x16', '\x17']:
                        result[j + 1] = ch
                        break
        elif has_underscore_before:
            # Look for underscore followed by mistranslation  
            for j in range(len(result) - 1):
                if result[j] == '_' and j + 1 < len(result):
                    next_ch = result[j + 1]
                    if next_ch in mistranslation_map and mistranslation_map[next_ch] == ch:
                        result[j + 1] = ch
                        break
                    elif is_format_char(next_ch) or ord(next_ch) < 32 or next_ch in ['\x16', '\x17']:
                        result[j + 1] = ch
                        break
    
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
