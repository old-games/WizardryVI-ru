# Wizardry VI

Russian translation project for Wizardry VI: Bane of the Cosmic Forge.

## Building

The project includes a build system to generate game archives from the parsed resources.

### Building locally

To build the game archives locally:

```bash
python3 tools/build.py
```

This will create:
- `build/en/` - English version game files
- `build/ru/` - Russian version game files
- `archives/wizardry6-en.zip` - English version archive
- `archives/wizardry6-ru.zip` - Russian version archive

### Build options

```bash
python3 tools/build.py --help
```

Options:
- `--output-dir DIR` - Output directory for build artifacts (default: `build`)
- `--archives-dir DIR` - Output directory for archives (default: `archives`)
- `--no-archives` - Skip creating ZIP archives

### CI/CD

The project uses GitHub Actions to automatically build game archives on every push to master. The built archives are available as workflow artifacts for 90 days.

## Useful information

### Overlays

- `WINIT` — title page, death screen;
- `WBASE` — main menu, game configuration;
- `WPCMK` — character menu;
- `WMAZE` — maze, including running away;
- `WPCVW` — review character, from maze and main menu, level up after fight;
— `WDOPT` — select spell to cast, item to use, from maze;
- `WMELE` — fight, first phase ("advance" messages);
- `WPOPS` — fight, party options;
— `WMEXE` — fight, execution log;
- `WTREA` — fight, end (?);
- `WMNPC` — NPC menu (?).
