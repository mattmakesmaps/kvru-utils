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
    @classmethod
    def setUpClass(self):
        try:
            os.mkdir(TEST_DATA_DEST)
        except FileExistsError:
            shutil.rmtree(TEST_DATA_DEST)

    def testConversion(self):
        """
        Perform conversion of files in source dir. Confirm that files
        matching our formats of interest were copied to dest dir, preserving
        the file structure.
        """
        ledger = Ledger(TEST_DATA_SOURCE, TEST_DATA_DEST)
        ledger.search_for_files()
        ledger.convert_all("192k")

        # Generate list of source files
        source_files = []
        for extension in ledger.INPUT_FORMATS:
            source_file_paths = list(TEST_DATA_SOURCE.rglob("*{}".format(extension)))
            source_files.extend(source_file_paths)

        # Generate list of dest files
        # and confirm their existence
        for source_file in source_files:
            source_relative_path = os.path.relpath(source_file, TEST_DATA_SOURCE)
            dest_relative_path = os.path.splitext(source_relative_path)[0] + ".mp3"
            dest_full_path = os.path.join(TEST_DATA_DEST, dest_relative_path)
            self.assertTrue(os.path.exists(dest_full_path))
    
    def testNonAudioFileOmitted(self):
        """
        Confirm that `BackupPlus.ico` was not copied to dest dir.
        Only copy those files that match our formats of interest.
        """
        icon_source = os.path.join(TEST_DATA_SOURCE, "BackupPlus.ico")
        self.assertTrue(os.path.exists(icon_source))
        icon_dest = os.path.join(TEST_DATA_DEST, "BackupPlus.ico")
        self.assertFalse(os.path.exists(icon_dest))

    @classmethod
    def tearDownClass(self):
        print("Tearing down {}".format(TEST_DATA_DEST))
        shutil.rmtree(TEST_DATA_DEST)

"""
MK FUTURE TEST:
- When future functionality is added to separate files with and without metadata,
  test that files are copied to correct destination. Will need to be implemented as
  a separate test class since destination structure will be different.
"""
