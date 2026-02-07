import json
import os
import unittest

import tools.database


class TestDatabase(unittest.TestCase):
    def test_read_messages_with_indices(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        with open(os.path.join(path, 'original', 'MISC.HDR'), 'rb') as f:
            huffman_table = f.read()
        self.assertEqual(len(huffman_table), 1024)

        with open(os.path.join(path, 'original', 'MSG.HDR'), 'rb') as f:
            indices = f.read()
        with open(os.path.join(path, 'original', 'MSG.DBS'), 'rb') as f:
            compressed = f.read()

        messages = tools.database.decode(compressed, huffman_table)
        for message in messages.values():
            self.assertIsInstance(message, bytes)

        messages = tools.database.reindex(messages, indices)

        with open(os.path.join(path, 'messages', 'messages.json'), 'r') as f:
            expected_messages = {k: v['en'] for k, v in json.load(f).items() if v['en'] is not None}

        self.assertEqual(len(messages), len(expected_messages))
        for index, message in messages.items():
            self.assertEqual(message.decode('ascii'), expected_messages[f'{index:05}'])

    @unittest.skip('TODO: scenario format is not finished')
    def test_read_scenario_with_indices(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        with open(os.path.join(path, 'original', 'MISC.HDR'), 'rb') as f:
            huffman_table = f.read()
        self.assertEqual(len(huffman_table), 1024)

        with open(os.path.join(path, 'original', 'SCENARIO.HDR'), 'rb') as f:
            indices = f.read()
        with open(os.path.join(path, 'original', 'SCENARIO.DBS'), 'rb') as f:
            compressed = f.read()

        scenario = tools.database.decode(compressed, huffman_table)
        for block in scenario.values():
            self.assertIsInstance(block, bytes)

        scenario = tools.database.reindex(scenario, indices)
        #for i, block in scenario.items():
        #    print(f'{i:05}: {len(block)}, {block[:30].hex()}')

        #with open(os.path.join(path, 'messages', 'scenario.json'), 'r') as f:
        #    expected_blocks = json.load(f)

        #self.assertEqual(len(scenario), len(expected_blocks))
        #for index, block in scenario.items():
        #    self.assertEqual(block.decode('ascii'), expected_blocks[f'{index:05}'])
