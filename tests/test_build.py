import os
import shutil
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

import tools.build


class TestBuild(unittest.TestCase):
    def setUp(self):
        """Set up temporary directories for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.build_dir = Path(self.test_dir) / 'build'
        self.archives_dir = Path(self.test_dir) / 'archives'
        
    def tearDown(self):
        """Clean up temporary directories."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_load_messages(self):
        """Test loading messages from JSON."""
        repo_root = Path(__file__).parent.parent
        messages_path = repo_root / 'messages' / 'messages.json'
        
        messages = tools.build.load_messages(str(messages_path))
        
        self.assertIn('en', messages)
        self.assertIn('ru', messages)
        self.assertIsInstance(messages['en'], dict)
        self.assertIsInstance(messages['ru'], dict)
        self.assertGreater(len(messages['en']), 0)
        self.assertGreater(len(messages['ru']), 0)
        
        # Check that messages are bytes
        for msg_id, msg in messages['en'].items():
            self.assertIsInstance(msg, bytes)
        for msg_id, msg in messages['ru'].items():
            self.assertIsInstance(msg, bytes)
    
    def test_load_items(self):
        """Test loading items from JSON."""
        repo_root = Path(__file__).parent.parent
        items_path = repo_root / 'items' / 'items.json'
        
        items = tools.build.load_items(str(items_path))
        
        self.assertIn('en', items)
        self.assertIn('ru', items)
        self.assertIsInstance(items['en'], list)
        self.assertIsInstance(items['ru'], list)
        self.assertGreater(len(items['en']), 0)
        self.assertGreater(len(items['ru']), 0)
        
        # Check that item data is bytes and has correct length
        for item in items['en']:
            self.assertIn('id', item)
            self.assertIn('data', item)
            self.assertIsInstance(item['data'], bytes)
            self.assertEqual(len(item['data']), 58)  # 0x3a
    
    def test_load_monsters(self):
        """Test loading monsters from JSON."""
        repo_root = Path(__file__).parent.parent
        monsters_path = repo_root / 'monsters' / 'monsters.json'
        
        monsters = tools.build.load_monsters(str(monsters_path))
        
        self.assertIn('en', monsters)
        self.assertIn('ru', monsters)
        self.assertIsInstance(monsters['en'], list)
        self.assertIsInstance(monsters['ru'], list)
        self.assertGreater(len(monsters['en']), 0)
        self.assertGreater(len(monsters['ru']), 0)
        
        # Check that monster data is bytes and has correct length
        for monster in monsters['en']:
            self.assertIn('id', monster)
            self.assertIn('data', monster)
            self.assertIsInstance(monster['data'], bytes)
            self.assertEqual(len(monster['data']), 158)  # 0x9e not 0xde
    
    def test_load_npcs(self):
        """Test loading NPCs from JSON."""
        repo_root = Path(__file__).parent.parent
        npcs_path = repo_root / 'npcs' / 'npcs.json'
        
        npcs = tools.build.load_npcs(str(npcs_path))
        
        self.assertIn('en', npcs)
        self.assertIn('ru', npcs)
        self.assertIsInstance(npcs['en'], list)
        self.assertIsInstance(npcs['ru'], list)
        self.assertGreater(len(npcs['en']), 0)
        self.assertGreater(len(npcs['ru']), 0)
        
        # Check that NPC data is bytes and has correct length
        for npc in npcs['en']:
            self.assertIn('id', npc)
            self.assertIn('data', npc)
            self.assertIsInstance(npc['data'], bytes)
            self.assertEqual(len(npc['data']), 126)  # 0x7e not 0x8e
    
    def test_encode_scenario(self):
        """Test encoding scenario data."""
        repo_root = Path(__file__).parent.parent
        
        # Load test data
        items = tools.build.load_items(str(repo_root / 'items' / 'items.json'))
        monsters = tools.build.load_monsters(str(repo_root / 'monsters' / 'monsters.json'))
        npcs = tools.build.load_npcs(str(repo_root / 'npcs' / 'npcs.json'))
        
        # Encode scenario
        scenario_data, disk_hdr = tools.build.encode_scenario(
            items['en'], monsters['en'], npcs['en']
        )
        
        self.assertIsInstance(scenario_data, bytes)
        self.assertIsInstance(disk_hdr, bytes)
        self.assertGreater(len(scenario_data), 0)
        self.assertEqual(len(disk_hdr), 4 + 10 * 4)  # 4 bytes header + 10 offsets
    
    def test_en_ru_different(self):
        """Test that EN and RU versions produce different files."""
        import tools.message
        
        repo_root = Path(__file__).parent.parent
        
        # Load data
        messages = tools.build.load_messages(str(repo_root / 'messages' / 'messages.json'))
        items = tools.build.load_items(str(repo_root / 'items' / 'items.json'))
        monsters = tools.build.load_monsters(str(repo_root / 'monsters' / 'monsters.json'))
        npcs = tools.build.load_npcs(str(repo_root / 'npcs' / 'npcs.json'))
        
        # Encode EN messages
        en_msg_data, _, _ = tools.message.encode(messages['en'])
        
        # Encode RU messages
        ru_msg_data, _, _ = tools.message.encode(messages['ru'])
        
        # Check that EN and RU messages are different
        self.assertNotEqual(en_msg_data, ru_msg_data)
        
        # Encode EN scenario
        en_scenario_data, _ = tools.build.encode_scenario(
            items['en'], monsters['en'], npcs['en']
        )
        
        # Encode RU scenario
        ru_scenario_data, _ = tools.build.encode_scenario(
            items['ru'], monsters['ru'], npcs['ru']
        )
        
        # Check that EN and RU scenarios are different
        self.assertNotEqual(en_scenario_data, ru_scenario_data)


if __name__ == '__main__':
    unittest.main()
