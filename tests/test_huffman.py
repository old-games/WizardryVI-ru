import os
import unittest

import tools.database


class TestHuffman(unittest.TestCase):
    def test_read_messages(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        with open(os.path.join(path, 'original', 'MISC.HDR'), 'rb') as f:
            huffman_table = f.read()
        self.assertEqual(len(huffman_table), 1024)

        with open(os.path.join(path, 'original', 'MSG.DBS'), 'rb') as f:
            compressed = f.read()

        messages = tools.database.decode(compressed, huffman_table)
        self.assertIsInstance(messages, dict)
        self.assertGreater(len(messages), 0)

        for message in messages.values():
            self.assertIsInstance(message, bytes)
            message.decode('ascii')
