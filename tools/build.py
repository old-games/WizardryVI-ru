#!/usr/bin/env python3
"""
Build script for Wizardry VI game archives.

This script builds the game from parsed resources (messages, items, monsters, npcs)
and creates two archives: one for English version and one for Russian version.
"""

import argparse
import json
import os
import subprocess
import sys
import zipfile
import shutil
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import tools.message
import tools.text


def load_messages(messages_path: str) -> dict[str, dict[int, bytes]]:
    """Load messages from JSON and return separate EN and RU dictionaries."""
    with open(messages_path, 'r', encoding='utf-8') as f:
        messages_data = json.load(f)
    
    en_messages = {}
    ru_messages = {}
    
    for msg_id_str, content in messages_data.items():
        msg_id = int(msg_id_str)
        
        # Handle EN messages
        if content['en'] is not None:
            en_text = content['en']
            if en_text.startswith('FIXME'):
                en_text = en_text[5:]
            en_messages[msg_id] = en_text.encode('ascii')
        
        # Handle RU messages
        ru_text = content['ru']
        if ru_text.startswith('FIXME'):
            ru_text = ru_text[5:]
        ru_messages[msg_id] = ru_text.encode('cp866')
    
    return {'en': en_messages, 'ru': ru_messages}


def load_items(items_path: str) -> dict[str, list[dict]]:
    """Load items from JSON and return separate EN and RU lists."""
    with open(items_path, 'r', encoding='utf-8') as f:
        items_data = json.load(f)
    
    en_items = []
    ru_items = []
    
    for item in items_data:
        # Decode raw hex data
        raw_data = bytes.fromhex(item['raw'])
        
        # Items have name at offset 0, length 16 bytes (null-terminated)
        en_name = tools.text.encode(item['name']['en'], 'ascii')
        ru_name = tools.text.encode(item['name']['ru'], 'cp866')
        
        # Pad or truncate to 16 bytes
        en_name = (en_name[:15] + b'\x00').ljust(16, b'\x00')
        ru_name = (ru_name[:15] + b'\x00').ljust(16, b'\x00')
        
        # Create modified raw data with new name
        en_item_data = en_name + raw_data[16:]
        ru_item_data = ru_name + raw_data[16:]
        
        en_items.append({'id': item['id'], 'data': en_item_data})
        ru_items.append({'id': item['id'], 'data': ru_item_data})
    
    return {'en': en_items, 'ru': ru_items}


def load_monsters(monsters_path: str) -> dict[str, list[dict]]:
    """Load monsters from JSON and return separate EN and RU lists."""
    with open(monsters_path, 'r', encoding='utf-8') as f:
        monsters_data = json.load(f)
    
    en_monsters = []
    ru_monsters = []
    
    for monster in monsters_data:
        # Decode raw hex data
        raw_data = bytes.fromhex(monster['raw'])
        
        # Monsters have multiple name fields, each 16 bytes
        # Offsets: 0x00 (name-singular), 0x10 (name-plural), 0x20 (hidden-name-singular), 0x30 (hidden-name-plural)
        en_name_singular = tools.text.encode(monster['name-singular']['en'], 'ascii')
        en_name_plural = tools.text.encode(monster['name-plural']['en'], 'ascii')
        en_hidden_singular = tools.text.encode(monster['hidden-name-singular']['en'], 'ascii')
        en_hidden_plural = tools.text.encode(monster['hidden-name-plural']['en'], 'ascii')
        
        ru_name_singular = tools.text.encode(monster['name-singular']['ru'], 'cp866')
        ru_name_plural = tools.text.encode(monster['name-plural']['ru'], 'cp866')
        ru_hidden_singular = tools.text.encode(monster['hidden-name-singular']['ru'], 'cp866')
        ru_hidden_plural = tools.text.encode(monster['hidden-name-plural']['ru'], 'cp866')
        
        # Pad or truncate to 16 bytes
        def pad_name(name: bytes) -> bytes:
            return (name[:15] + b'\x00').ljust(16, b'\x00')
        
        en_names = pad_name(en_name_singular) + pad_name(en_name_plural) + pad_name(en_hidden_singular) + pad_name(en_hidden_plural)
        ru_names = pad_name(ru_name_singular) + pad_name(ru_name_plural) + pad_name(ru_hidden_singular) + pad_name(ru_hidden_plural)
        
        # Create modified raw data with new names
        en_monster_data = en_names + raw_data[64:]
        ru_monster_data = ru_names + raw_data[64:]
        
        en_monsters.append({'id': monster['id'], 'data': en_monster_data})
        ru_monsters.append({'id': monster['id'], 'data': ru_monster_data})
    
    return {'en': en_monsters, 'ru': ru_monsters}


def load_npcs(npcs_path: str) -> dict[str, list[dict]]:
    """Load NPCs from JSON and return separate EN and RU lists."""
    with open(npcs_path, 'r', encoding='utf-8') as f:
        npcs_data = json.load(f)
    
    en_npcs = []
    ru_npcs = []
    
    for npc in npcs_data:
        # Decode raw hex data
        raw_data = bytes.fromhex(npc['raw'])
        
        # NPCs have name at offset 0, length 32 bytes (null-terminated)
        en_name = tools.text.encode(npc['name']['en'], 'ascii')
        ru_name = tools.text.encode(npc['name']['ru'], 'cp866')
        
        # Pad or truncate to 32 bytes
        en_name = (en_name[:31] + b'\x00').ljust(32, b'\x00')
        ru_name = (ru_name[:31] + b'\x00').ljust(32, b'\x00')
        
        # Create modified raw data with new name
        en_npc_data = en_name + raw_data[32:]
        ru_npc_data = ru_name + raw_data[32:]
        
        en_npcs.append({'id': npc['id'], 'data': en_npc_data})
        ru_npcs.append({'id': npc['id'], 'data': ru_npc_data})
    
    return {'en': en_npcs, 'ru': ru_npcs}


def encode_scenario(items: list[dict], monsters: list[dict], npcs: list[dict]) -> tuple[bytes, bytes]:
    """
    Encode items, monsters, and NPCs into SCENARIO.DBS and DISK.HDR format.
    
    Based on tools/scenario.py, the scenario file has blocks:
    - Block 0: EXPERIENCE (0x0e * 4 * 16 bytes)
    - Block 1: ITEM (multiple of 0x4a bytes)
    - Block 4: MONSTER (multiple of 0xde bytes)
    - Block 5: NPC (multiple of 0x8e bytes)
    """
    # Sort by ID to ensure proper order
    items = sorted(items, key=lambda x: x['id'])
    monsters = sorted(monsters, key=lambda x: x['id'])
    npcs = sorted(npcs, key=lambda x: x['id'])
    
    # Build data blocks
    # Note: We're assuming experience block is empty or not needed for the translation
    # If needed, it should be loaded from original
    experience_block = b'\x00' * (0x0e * 4 * 16)  # Empty experience block
    
    # Items block
    item_block = b''.join(item['data'] for item in items)
    
    # Monsters block
    monster_block = b''.join(monster['data'] for monster in monsters)
    
    # NPCs block
    npc_block = b''.join(npc['data'] for npc in npcs)
    
    # Build scenario data (blocks 0-9, we only modify 1, 4, 5)
    # We need to preserve other blocks from the original scenario
    # For now, create empty blocks for 2, 3, 6, 7, 8, 9
    blocks = [
        experience_block,  # 0
        item_block,        # 1
        b'',               # 2
        b'',               # 3
        monster_block,     # 4
        npc_block,         # 5
        b'',               # 6
        b'',               # 7
        b'',               # 8
        b'',               # 9
    ]
    
    # Build offsets for DISK.HDR
    offsets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    current_offset = 0
    for i, block in enumerate(blocks):
        offsets[i] = current_offset
        current_offset += len(block)
    
    # Build DISK.HDR format
    disk_hdr = b'\x00' * 4  # First 4 bytes are zeros
    for offset in offsets:
        disk_hdr += offset.to_bytes(4, 'little')
    
    # Build scenario data
    scenario_data = b''.join(blocks)
    
    return scenario_data, disk_hdr


def build_version(output_dir: Path, language: str, messages: dict[int, bytes], 
                  items: list[dict], monsters: list[dict], npcs: list[dict],
                  original_dir: Path):
    """Build game files for a specific language version."""
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Building {language.upper()} version...")
    
    # Build messages
    print("  Encoding messages...")
    msg_data, msg_indices, misc_hdr = tools.message.encode(messages)
    
    # Write message files
    (output_dir / 'MSG.DBS').write_bytes(msg_data)
    (output_dir / 'MSG.HDR').write_bytes(msg_indices)
    (output_dir / 'MISC.HDR').write_bytes(misc_hdr)
    
    # Build scenario
    print("  Encoding scenario (items, monsters, NPCs)...")
    scenario_data, disk_hdr = encode_scenario(items, monsters, npcs)
    
    # Write scenario files
    (output_dir / 'SCENARIO.DBS').write_bytes(scenario_data)
    (output_dir / 'DISK.HDR').write_bytes(disk_hdr)
    
    # Copy other necessary files from original directory
    print("  Copying other game files...")
    files_to_copy = [
        '*.OVR', '*.EXE', '*.DRV', '*.PIC', '*.SND',
        'WFONT*.CGA', 'WFONT*.EGA', 'WFONT*.T16',
        'WPORT*.CGA', 'WPORT*.EGA', 'WPORT*.T16',
        '*.CGA', '*.EGA', '*.T16', 'SCEN*.DBS', 'SCEN*.HDR',
        'DISK*.HDR', 'MASTER.HDR', 'SCENARIO.HDR', 'MAZEDATA.*'
    ]
    
    import glob
    for pattern in files_to_copy:
        for file in glob.glob(str(original_dir / pattern)):
            filename = os.path.basename(file)
            # Don't overwrite files we just created
            if filename not in ['MSG.DBS', 'MSG.HDR', 'MISC.HDR', 'SCENARIO.DBS', 'DISK.HDR']:
                shutil.copy2(file, output_dir / filename)
    
    print(f"  {language.upper()} version built successfully in {output_dir}")


def get_git_commit_hash() -> str:
    """Get the short git commit hash (7 characters)."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short=7', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # If git is not available or not in a git repo, return a placeholder
        return 'unknown'


def create_archive(build_dir: Path, archive_path: Path, language: str, archive_root_name: str):
    """Create a ZIP archive from the build directory with a root directory inside."""
    print(f"Creating {language.upper()} archive...")
    
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in build_dir.glob('*'):
            if file.is_file():
                # Add file with archive_root_name as the root directory
                arcname = f"{archive_root_name}/{file.name}"
                zipf.write(file, arcname)
    
    print(f"  Archive created: {archive_path}")
    print(f"  Archive size: {archive_path.stat().st_size / 1024 / 1024:.2f} MB")


def main():
    parser = argparse.ArgumentParser(
        description='Build Wizardry VI game archives from parsed resources'
    )
    parser.add_argument(
        '--output-dir',
        default='build',
        help='Output directory for build artifacts (default: build)'
    )
    parser.add_argument(
        '--archives-dir',
        default='archives',
        help='Output directory for archives (default: archives)'
    )
    parser.add_argument(
        '--no-archives',
        action='store_true',
        help='Skip creating ZIP archives'
    )
    
    args = parser.parse_args()
    
    # Get repository root
    repo_root = Path(__file__).parent.parent
    
    # Define paths
    messages_path = repo_root / 'messages' / 'messages.json'
    items_path = repo_root / 'items' / 'items.json'
    monsters_path = repo_root / 'monsters' / 'monsters.json'
    npcs_path = repo_root / 'npcs' / 'npcs.json'
    original_dir = repo_root / 'original'
    
    build_base = repo_root / args.output_dir
    archives_base = repo_root / args.archives_dir
    
    # Check that all required files exist
    for path in [messages_path, items_path, monsters_path, npcs_path, original_dir]:
        if not path.exists():
            print(f"Error: Required path not found: {path}", file=sys.stderr)
            return 1
    
    # Load data
    print("Loading data...")
    messages = load_messages(messages_path)
    items = load_items(items_path)
    monsters = load_monsters(monsters_path)
    npcs = load_npcs(npcs_path)
    
    # Build EN version
    en_build_dir = build_base / 'en'
    build_version(en_build_dir, 'en', messages['en'], items['en'], 
                  monsters['en'], npcs['en'], original_dir)
    
    # Build RU version
    ru_build_dir = build_base / 'ru'
    build_version(ru_build_dir, 'ru', messages['ru'], items['ru'],
                  monsters['ru'], npcs['ru'], original_dir)
    
    # Create archives if requested
    if not args.no_archives:
        archives_base.mkdir(parents=True, exist_ok=True)
        
        # Get git commit hash for archive naming
        commit_hash = get_git_commit_hash()
        
        # Archive naming: WizardryVI-ru-{hash}[data=english].zip for EN, WizardryVI-ru-{hash}.zip for RU
        en_archive_name = f'WizardryVI-ru-{commit_hash}[data=english]'
        ru_archive_name = f'WizardryVI-ru-{commit_hash}'
        
        en_archive = archives_base / f'{en_archive_name}.zip'
        create_archive(en_build_dir, en_archive, 'en', en_archive_name)
        
        ru_archive = archives_base / f'{ru_archive_name}.zip'
        create_archive(ru_build_dir, ru_archive, 'ru', ru_archive_name)
    
    print("\nBuild completed successfully!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
