# Package import pattern REF: https://docs.python-guide.org/writing/structure/#test-suite
import os
import pathlib
import shutil
from context import mp3convert
from mp3convert import Ledger

import unittest

TEST_DATA_DEST = pathlib.Path(os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_data', 'dest')))
TEST_DATA_SOURCE = pathlib.Path(os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_data', 'source')))

class TestLedger(unittest.TestCase):
    def setUpClass(self):
        os.mkdir(TEST_DATA_DEST)

    def testConversion(self):
        ledger = Ledger(TEST_DATA_SOURCE, TEST_DATA_DEST)
        ledger.search_for_files()
        ledger.convert_all("192k")
    
    """
    MK TESTS:
    - non music files are not copied.
    - check that files from root and subdirs are copied correctly.
    """

    def tearDownClass(self):
        print("Tearing down {}".format(TEST_DATA_DEST))
        shutil.rmtree(TEST_DATA_DEST)

"""
MK FUTURE TEST:
- When future functionality is added to separate files with and without metadata,
  test that files are copied to correct destination. Will need to be implemented as
  a separate test class since destination structure will be different.
"""
