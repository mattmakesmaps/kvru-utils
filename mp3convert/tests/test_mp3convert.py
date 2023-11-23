# Package import pattern REF: https://docs.python-guide.org/writing/structure/#test-suite
from context import mp3convert
from mp3convert import Ledger

import unittest

class TestLedger(unittest.TestCase):

    def testLedger(self):
        self.assertEqual(1, 1)