#!/usr/bin/env python3
'''
Build script for Wizardry VI game archives.

This script builds the game from parsed resources (messages, items, monsters, npcs)
and creates two archives: one for English version and one for Russian version.
'''

import argparse
import glob
import json
import os
import subprocess
import sys
import zipfile
import shutil

import tools.message
import tools.text
import tools.ega
import tools.tandy
import tools.rle
import tools.picture
import tools.maze
import tools.tenfold

import PIL.Image


def load_messages(messages_path: str) -> dict[str, dict[int, bytes]]:
    '''
    Load messages from JSON and return separate EN and RU dictionaries.
    '''

    with open(messages_path, 'r', encoding='utf-8') as f:
        messages_data = json.load(f)

    en_messages = {}
    ru_messages = {}

    for msg_id_str, content in messages_data.items():
        msg_id = int(msg_id_str)

        # Handle EN messages.
        if content['en'] is not None:
            en_text = content['en']
            if en_text.startswith('FIXME'):
                en_text = en_text[5:]
            en_messages[msg_id] = en_text.encode('ascii')

        # Handle RU messages.
        ru_text = content['ru']
        if ru_text.startswith('FIXME'):
            ru_text = ru_text[5:]
        ru_messages[msg_id] = ru_text.encode('cp866')

    return {'en': en_messages, 'ru': ru_messages}


def load_items(items_path: str) -> dict[str, list[dict]]:
    '''
    Load items from JSON and return separate EN and RU lists.
    '''

    with open(items_path, 'r', encoding='utf-8') as f:
        items_data = json.load(f)

    en_items = []
    ru_items = []

    for item in items_data:
        # Decode raw hex data.
        raw_data = bytes.fromhex(item['raw'])

        # Items have name at offset 0, length 16 bytes (null-terminated).
        en_name = tools.text.encode(item['name']['en'], 'ascii')
        ru_name = tools.text.encode(item['name']['ru'], 'cp866')

        # Pad or truncate to 16 bytes.
        en_name = (en_name[:15] + b'\x00').ljust(16, b'\x00')
        ru_name = (ru_name[:15] + b'\x00').ljust(16, b'\x00')

        # Create modified raw data with new name.
        en_item_data = en_name + raw_data[16:]
        ru_item_data = ru_name + raw_data[16:]

        en_items.append({'id': item['id'], 'data': en_item_data})
        ru_items.append({'id': item['id'], 'data': ru_item_data})

    return {'en': en_items, 'ru': ru_items}


def load_monsters(monsters_path: str) -> dict[str, list[dict]]:
    '''
    Load monsters from JSON and return separate EN and RU lists.
    '''

    with open(monsters_path, 'r', encoding='utf-8') as f:
        monsters_data = json.load(f)

    en_monsters = []
    ru_monsters = []

    for monster in monsters_data:
        # Decode raw hex data.
        raw_data = bytes.fromhex(monster['raw'])

        # Monsters have multiple name fields, each 16 bytes.
        # Offsets: `0x00` (name-singular), `0x10` (name-plural), `0x20` (hidden-name-singular), `0x30` (hidden-name-plural).
        en_name_singular = tools.text.encode(monster['name-singular']['en'], 'ascii')
        en_name_plural = tools.text.encode(monster['name-plural']['en'], 'ascii')
        en_hidden_singular = tools.text.encode(monster['hidden-name-singular']['en'], 'ascii')
        en_hidden_plural = tools.text.encode(monster['hidden-name-plural']['en'], 'ascii')

        ru_name_singular = tools.text.encode(monster['name-singular']['ru'], 'cp866')
        ru_name_plural = tools.text.encode(monster['name-plural']['ru'], 'cp866')
        ru_hidden_singular = tools.text.encode(monster['hidden-name-singular']['ru'], 'cp866')
        ru_hidden_plural = tools.text.encode(monster['hidden-name-plural']['ru'], 'cp866')

        # Pad or truncate to 16 bytes.
        def pad_name(name: bytes) -> bytes:
            return (name[:15] + b'\x00').ljust(16, b'\x00')

        en_names = pad_name(en_name_singular) + pad_name(en_name_plural) + pad_name(en_hidden_singular) + pad_name(en_hidden_plural)
        ru_names = pad_name(ru_name_singular) + pad_name(ru_name_plural) + pad_name(ru_hidden_singular) + pad_name(ru_hidden_plural)

        # Create modified raw data with new names.
        en_monster_data = en_names + raw_data[64:]
        ru_monster_data = ru_names + raw_data[64:]

        en_monsters.append({'id': monster['id'], 'data': en_monster_data})
        ru_monsters.append({'id': monster['id'], 'data': ru_monster_data})

    return {'en': en_monsters, 'ru': ru_monsters}


def load_npcs(npcs_path: str) -> dict[str, list[dict]]:
    '''
    Load NPCs from JSON and return separate EN and RU lists.
    '''

    with open(npcs_path, 'r', encoding='utf-8') as f:
        npcs_data = json.load(f)

    en_npcs = []
    ru_npcs = []

    for npc in npcs_data:
        # Decode raw hex data.
        raw_data = bytes.fromhex(npc['raw'])

        # NPCs have name at offset 0, length 32 bytes (null-terminated).
        en_name = tools.text.encode(npc['name']['en'], 'ascii')
        ru_name = tools.text.encode(npc['name']['ru'], 'cp866')

        # Pad or truncate to 32 bytes.
        en_name = (en_name[:31] + b'\x00').ljust(32, b'\x00')
        ru_name = (ru_name[:31] + b'\x00').ljust(32, b'\x00')

        # Create modified raw data with new name.
        en_npc_data = en_name + raw_data[32:]
        ru_npc_data = ru_name + raw_data[32:]

        en_npcs.append({'id': npc['id'], 'data': en_npc_data})
        ru_npcs.append({'id': npc['id'], 'data': ru_npc_data})

    return {'en': en_npcs, 'ru': ru_npcs}


def encode_scenario(items: list[dict], monsters: list[dict], npcs: list[dict]) -> tuple[bytes, bytes]:
    '''
    Encode items, monsters, and NPCs into SCENARIO.DBS and DISK.HDR format.

    Based on tools/scenario.py, the scenario file has blocks:
    - Block 0: EXPERIENCE (0x0e * 4 * 16 bytes)
    - Block 1: ITEM (multiple of 0x4a bytes)
    - Block 4: MONSTER (multiple of 0xde bytes)
    - Block 5: NPC (multiple of 0x8e bytes)
    '''

    # Sort by ID to ensure proper order.
    items = sorted(items, key=lambda x: x['id'])
    monsters = sorted(monsters, key=lambda x: x['id'])
    npcs = sorted(npcs, key=lambda x: x['id'])

    # Build data blocks.
    # Note: We're assuming experience block is empty or not needed for the translation
    # If needed, it should be loaded from original
    experience_block = b'\x00' * (0x0e * 4 * 16)  # Empty experience block

    # Items block.
    item_block = b''.join(item['data'] for item in items)

    # Monsters block.
    monster_block = b''.join(monster['data'] for monster in monsters)

    # NPCs block.
    npc_block = b''.join(npc['data'] for npc in npcs)

    # Build scenario data (blocks 0-9, we only modify 1, 4, 5).
    # We need to preserve other blocks from the original scenario.
    # For now, create empty blocks for 2, 3, 6, 7, 8, 9.
    blocks = [
        experience_block, # 0
        item_block,       # 1
        b'',              # 2
        b'',              # 3
        monster_block,    # 4
        npc_block,        # 5
        b'',              # 6
        b'',              # 7
        b'',              # 8
        b'',              # 9
    ]

    # Build offsets for `DISK.HDR`.
    offsets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    current_offset = 0
    for i, block in enumerate(blocks):
        offsets[i] = current_offset
        current_offset += len(block)

    # Build `DISK.HDR` format.
    disk_hdr = b'\x00' * 4 # First 4 bytes are zeros.
    for offset in offsets:
        disk_hdr += offset.to_bytes(4, 'little')

    # Build scenario data.
    scenario_data = b''.join(blocks)

    return scenario_data, disk_hdr


def build_version(output_dir: str, language: str, messages: dict[int, bytes], 
                  items: list[dict], monsters: list[dict], npcs: list[dict],
                  original_dir: str):
    '''
    Build game files for a specific language version.
    '''

    # Create output directory.
    os.makedirs(output_dir, exist_ok=True)

    print(f'Building {language.upper()} version...')

    # Build messages.
    print('  Encoding messages...')
    msg_data, msg_indices, misc_hdr = tools.message.encode(messages)

    # Write message files.
    with open(os.path.join(output_dir, 'MSG.DBS'), 'wb') as f:
        f.write(msg_data)
    with open(os.path.join(output_dir, 'MSG.HDR'), 'wb') as f:
        f.write(msg_indices)
    with open(os.path.join(output_dir, 'MISC.HDR'), 'wb') as f:
        f.write(misc_hdr)

    # Build scenario.
    print('  Encoding scenario (items, monsters, NPCs)...')
    scenario_data, disk_hdr = encode_scenario(items, monsters, npcs)

    # Write scenario files.
    with open(os.path.join(output_dir, 'SCENARIO.DBS'), 'wb') as f:
        f.write(scenario_data)
    with open(os.path.join(output_dir, 'DISK.HDR'), 'wb') as f:
        f.write(disk_hdr)

    # Build patched pictures (EGA/T16 screens, MAZEDATA, and PIC archives).
    print('  Encoding patched pictures (if any)...')
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _encode_patched_pictures(
        repo_root=repo_root,
        original_dir=original_dir,
        output_dir=output_dir,
        language=language,
    )

    # Copy other necessary files from original directory.
    print('  Copying other game files...')
    files_to_copy = [
        '*.OVR',
        '*.EXE',
        '*.DRV',
        '*.PIC',
        '*.SND',
        'WFONT*.CGA',
        'WFONT*.EGA',
        'WFONT*.T16',
        'WPORT*.CGA',
        'WPORT*.EGA',
        'WPORT*.T16',
        '*.CGA',
        '*.EGA',
        '*.T16',
        'SCEN*.DBS',
        'SCEN*.HDR',
        'DISK*.HDR',
        'MASTER.HDR',
        'SCENARIO.HDR',
        'MAZEDATA.*',
    ]

    for pattern in files_to_copy:
        for file in glob.glob(os.path.join(original_dir, pattern)):
            filename = os.path.basename(file)
            # Don't overwrite files we just created.
            if filename not in ['MSG.DBS', 'MSG.HDR', 'MISC.HDR', 'SCENARIO.DBS', 'DISK.HDR', 'MAZEDATA.EGA', 'MAZEDATA.CGA', 'MAZEDATA.T16', 'CREDITS.PIC', 'DRAGONSC.EGA', 'DRAGONSC.CGA', 'DRAGONSC.T16']:
                shutil.copy2(file, os.path.join(output_dir, filename))

    print(f'  {language.upper()} version built successfully in {output_dir}')


def _iter_override_pngs(repo_root: str, language: str) -> list[str]:
    '''
    Return a sorted list of override PNGs for a given language.

    Conventions:
    - RU overrides are stored as `*.ru.png`.
    - EN overrides are stored as `*.png` but *excluding* `*.ru.png`.
    - We only look under `ega/`, `tandy/`, and `pictures/` trees.
    '''

    search_roots = [os.path.join(repo_root, 'ega'), os.path.join(repo_root, 'tandy'), os.path.join(repo_root, 'pictures')]
    candidates: list[str] = []
    for sr in search_roots:
        if not os.path.exists(sr):
            continue
        candidates.extend(glob.glob(os.path.join(sr, '**', '*.png'), recursive=True))

    if language == 'ru':
        overrides = [p for p in candidates if p.endswith('.ru.png')]
    else:
        overrides = [p for p in candidates if p.endswith('.png') and not p.endswith('.ru.png')]

    # Deduplicate while preserving deterministic order.
    return sorted(set(overrides))


def _strip_language_suffix(path: str, language: str) -> str:
    base = os.path.basename(path)
    if language == 'ru' and base.endswith('.ru.png'):
        base = base[:-len('.ru.png')] + '.png'
        return os.path.join(os.path.dirname(path), base)
    return path


def _encode_patched_pictures(*, repo_root: str, original_dir: str, output_dir: str, language: str) -> None:
    '''Encode/pack all picture overrides into game binaries in output_dir.'''

    overrides = _iter_override_pngs(repo_root, language)
    if not overrides:
        return

    # Buckets.
    direct_files: dict[str, str] = {} # E.g. `DRAGONSC.EGA` -> png
    mazedata_overrides: dict[str, dict[int, str]] = {} # E.g. `MAZEDATA.EGA` -> {idx: png}
    pic_overrides: dict[str, dict[int, str]] = {} # E.g. `CREDITS.PIC` -> {idx: png}

    for p in overrides:
        # Normalize name without language suffix.
        name = os.path.basename(p) # E.g. `MAZEDATA.EGA.148.ru.png`.
        stripped = os.path.basename(_strip_language_suffix(p, language))

        # `MAZEDATA` overrides are stored under `*/maze/` and named: `MAZEDATA.EGA.148[.ru].png`
        if stripped.startswith('MAZEDATA.') and stripped.endswith('.png') and stripped.count('.') >= 3:
            base, idx_str, _ = stripped.rsplit('.', 2)
            try:
                idx = int(idx_str)
            except ValueError:
                idx = None
            if idx is not None:
                mazedata_overrides.setdefault(base, {})[idx] = p
                continue

        # `PIC` frames are stored as `NAME.00.PIC[.ru].png`
        if stripped.endswith('.PIC.png') and '.' in stripped:
            base, _, _ = stripped.rsplit('.', 2)  # strip .PIC.png
            if '.' in base:
                pic_name, idx_str = base.rsplit('.', 1)
                try:
                    idx = int(idx_str)
                except ValueError:
                    idx = None
                if idx is not None:
                    pic_overrides.setdefault(f'{pic_name}.PIC', {})[idx] = p
                    continue

        # Direct screen override, e.g. `ega/DRAGONSC.EGA[.ru].png` -> `DRAGONSC.EGA`.
        if stripped.endswith('.EGA.png'):
            direct_files[stripped[:-len('.png')]] = p
            continue
        if stripped.endswith('.T16.png'):
            direct_files[stripped[:-len('.png')]] = p
            continue

    # Encode direct files.
    for target_name, png_path in sorted(direct_files.items()):
        orig_path = os.path.join(original_dir, target_name)
        if not os.path.exists(orig_path):
            raise FileNotFoundError(f'Original file not found for override: {orig_path}')
        with PIL.Image.open(png_path) as img:
            img = tools.tenfold.decode(img)
            if target_name.upper().endswith('.EGA'):
                encoded = tools.ega.encode(img, pad_size=0x400)
            elif target_name.upper().endswith('.T16'):
                encoded = tools.tandy.encode(img, pad_size=0x400)
            else:
                continue
        with open(os.path.join(output_dir, target_name), 'wb') as f:
            f.write(encoded)

    # Encode PIC archives.
    for pic_name, frames in sorted(pic_overrides.items()):
        orig_path = os.path.join(original_dir, pic_name)
        if not os.path.exists(orig_path):
            raise FileNotFoundError(f'Original file not found for override: {orig_path}')

        with open(orig_path, 'rb') as f:
            compressed = f.read()
        uncompressed = tools.rle.decompress(compressed)
        images = tools.picture.decode(uncompressed)

        for idx, png_path in frames.items():
            if idx >= len(images):
                raise IndexError(f'PIC override index {idx} out of range for {pic_name} (has {len(images)} frames).')
            with PIL.Image.open(png_path) as img:
                images[idx] = tools.tenfold.decode(img)

        new_uncompressed = tools.picture.encode(images, warn_on_non_palette=True)
        # Preserve trailing zeros used in original `CREDITS.PIC`. FIXME
        if pic_name.upper() == 'CREDITS.PIC' and len(uncompressed) > len(new_uncompressed):
            tail = uncompressed[len(new_uncompressed):]
            if set(tail) == {0}:
                new_uncompressed = new_uncompressed + tail

        new_compressed = tools.rle.compress(new_uncompressed)
        with open(os.path.join(output_dir, pic_name), 'wb') as f:
            f.write(new_compressed)

    # Encode `MAZEDATA` containers.
    for mazedata_name, tiles in sorted(mazedata_overrides.items()):
        orig_path = os.path.join(original_dir, mazedata_name)
        if not os.path.exists(orig_path):
            raise FileNotFoundError(f'Original file not found for override: {orig_path}')
        with open(orig_path, 'rb') as f:
            data = f.read()

        data_payload, object_table = tools.maze.decode(data)
        # Determine encoder based on variant.
        if mazedata_name.endswith('.EGA'):
            encode_img = tools.ega.encode
        elif mazedata_name.endswith('.T16'):
            encode_img = tools.tandy.encode
        else:
            # CGA overrides not requested for now.
            continue

        new_payload: list[tuple[int, int, bytes]] = []
        for idx, (w, h, payload) in enumerate(data_payload):
            if idx in tiles:
                with PIL.Image.open(tiles[idx]) as img:
                    img = tools.tenfold.decode(img)
                    payload = encode_img(img)
            new_payload.append((w, h, payload))

        new_data = tools.maze.encode(new_payload, object_table)
        with open(os.path.join(output_dir, mazedata_name), 'wb') as f:
            f.write(new_data)


def get_git_commit_hash() -> str:
    '''
    Get the short git commit hash.
    '''

    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # If git is not available or not in a git repo, return a placeholder.
        return 'unknown'


def create_archive(build_dir: str, archive_path: str, language: str, archive_root_name: str):
    '''
    Create a ZIP archive from the build directory with a root directory inside.
    '''

    print(f'Creating {language.upper()} archive...')

    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(build_dir):
            file_path = os.path.join(build_dir, filename)
            if os.path.isfile(file_path):
                # Add file with archive_root_name as the root directory.
                arcname = f'{archive_root_name}/{filename}'
                zipf.write(file_path, arcname)

    print(f'  Archive created: {archive_path}')
    print(f'  Archive size: {os.path.getsize(archive_path) / 1024 / 1024:.2f} MB')


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
    parser.add_argument(
        '--language',
        required=True,
        choices=['en', 'ru'],
        help='Language to build: en or ru'
    )

    args = parser.parse_args()

    # Get repository root.
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define paths.
    messages_path = os.path.join(repo_root, 'messages', 'messages.json')
    items_path = os.path.join(repo_root, 'items', 'items.json')
    monsters_path = os.path.join(repo_root, 'monsters', 'monsters.json')
    npcs_path = os.path.join(repo_root, 'npcs', 'npcs.json')
    original_dir = os.path.join(repo_root, 'original')

    build_base = os.path.join(repo_root, args.output_dir)
    archives_base = os.path.join(repo_root, args.archives_dir)

    # Check that all required files exist.
    for path in [messages_path, items_path, monsters_path, npcs_path, original_dir]:
        if not os.path.exists(path):
            print(f'Error: Required path not found: {path}', file=sys.stderr)
            return 1

    # Load data.
    print('Loading data...')
    messages = load_messages(messages_path)
    items = load_items(items_path)
    monsters = load_monsters(monsters_path)
    npcs = load_npcs(npcs_path)

    # Build the requested version.
    if args.language == 'en':
        build_dir = os.path.join(build_base, 'en')
        build_version(build_dir, 'en', messages['en'], items['en'], monsters['en'], npcs['en'], original_dir)
    else: # RU.
        build_dir = os.path.join(build_base, 'ru')
        build_version(build_dir, 'ru', messages['ru'], items['ru'], monsters['ru'], npcs['ru'], original_dir)

    # Create archives if requested.
    if not args.no_archives:
        os.makedirs(archives_base, exist_ok=True)

        # Get git commit hash for archive naming.
        commit_hash = get_git_commit_hash()

        # Archive naming: `WizardryVI-ru-{hash}[data=english].zip` for EN, `WizardryVI-ru-{hash}.zip` for RU.
        if args.language == 'en':
            archive_name = f'WizardryVI-ru-{commit_hash}[data=english]'
            archive_path = os.path.join(archives_base, f'{archive_name}.zip')
            create_archive(build_dir, archive_path, 'en', archive_name)
        else: # RU.
            archive_name = f'WizardryVI-ru-{commit_hash}'
            archive_path = os.path.join(archives_base, f'{archive_name}.zip')
            create_archive(build_dir, archive_path, 'ru', archive_name)

    print('\nBuild completed successfully!')
    return 0


if __name__ == '__main__':
    sys.exit(main())
