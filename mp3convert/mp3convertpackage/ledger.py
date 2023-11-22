"""ledger class which manages processing of individual music files."""
import csv
import logging
import os
import shutil

from mp3convertpackage.utils import convert_to_mp3
from mp3convertpackage.musicfile import MusicFile

logger = logging.getLogger("mp3convert.ledger")

class Ledger:
    """
    A class that represents a ledger of music files.

    Attributes:
    - source_root: The root directory to search for music files.
    - dest_root: The root directory to write converted files to.
    - checksum_csv_path: The path to a CSV file to log checksums to.
    - files: A list of MusicFile objects.
    - INPUT_FORMATS: A tuple of input file formats that the class searches for.
    """

    def __init__(self, source_root, dest_root, checksum_csv_path=None):
        self.source_root = source_root
        self.dest_root = dest_root
        self.checksum_csv_path = checksum_csv_path
        self.files = []
        self.INPUT_FORMATS = (".mp3", ".wav", ".aif", ".aiff")

    def _log_checksum(self, checksum, source_filename, dest_filename):
        with open(self.checksum_csv_path, "a", encoding="utf-8") as csvfile:
            checksum_writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            checksum_writer.writerow([checksum, source_filename, dest_filename])

    def search_for_files(self):
        """
        Recursively search an input directory. Populate self.files with MusicFile objects.
        """
        for extension in self.INPUT_FORMATS:
            found_music_file_paths = list(self.source_root.rglob("*{}".format(extension)))
            found_music_files = [MusicFile(path) for path in found_music_file_paths]
            self.files.extend(found_music_files)

    def convert_all(self, bitrate):
        """
        Convert all files in self.files to mp3 format and write them to outputdir.

        - Existing MP3s will be copied directly to outputdir.
        """
        for music_file in self.files:
            # Create absolute path to output file
            source_relative_path = os.path.relpath(music_file.filepath, self.source_root)
            dest_relative_path = os.path.splitext(source_relative_path)[0] + ".mp3"
            dest_full_path = os.path.join(self.dest_root, dest_relative_path)

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

            if self.checksum_csv_path:
                source_filename = os.path.basename(source_relative_path)
                dest_filename = os.path.splitext(source_filename)[0] + ".mp3"
                self._log_checksum(music_file.checksum, source_filename, dest_filename)
