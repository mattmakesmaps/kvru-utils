"""Ledger class which manages processing of individual music files."""
import logging
import os
import shutil

from musicfile import MusicFile
from utils import convert_to_mp3

logger = logging.getLogger("mp3-convert.ledger")


class Ledger:
    """
    A class that represents a ledger of music files.

    Attributes:
    - files: A list of MusicFile objects.
    - INPUT_FORMATS: A tuple of input file formats that the class searches for.
    """

    def __init__(self):
        self.files = []
        self.INPUT_FORMATS = (".mp3", ".wav", ".aif", ".aiff")

    def search_for_files(self, inputdir):
        """
        Recursively search an input directory. Populate self.files with MusicFile objects.
        """
        for extension in self.INPUT_FORMATS:
            found_music_file_paths = list(inputdir.rglob("*{}".format(extension)))
            found_music_files = [MusicFile(path) for path in found_music_file_paths]
            self.files.extend(found_music_files)

    def convert_all(self, source_root, dest_root, bitrate):
        """
        Convert all files in self.files to mp3 format and write them to outputdir.
        """
        for music_file in self.files:
            # Create absolute path to output file
            source_relative_path = os.path.relpath(music_file.filepath, source_root)
            source_relative_path = os.path.splitext(source_relative_path)[0] + ".mp3"
            dest_full_path = os.path.join(dest_root, source_relative_path)

            if os.path.exists(dest_full_path):
                logger.info(
                    "Skipping %s because it already exists", dest_full_path
                )
                continue

            if not os.path.exists(os.path.dirname(dest_full_path)):
                os.makedirs(os.path.dirname(dest_full_path))

            if music_file.filepath.suffix == ".mp3":
                logger.info("Copying existing MP3 %s", dest_full_path)
                shutil.copyfile(music_file.filepath, dest_full_path)
            else:
                convert_to_mp3(music_file.filepath, dest_full_path, bitrate)
