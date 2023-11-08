import logging
import os
import shutil

from MusicFile import MusicFile
from utils import convert_to_mp3

logger = logging.getLogger('mp3-convert.ledger')

class Ledger:
    def __init__(self):
        self.files = []
        self.INPUT_FORMATS = ('.mp3', '.wav', '.aiff')

    def searchForFiles(self, inputdir):
        """
        Recursively search an input directory. Populate self.files with MusicFile objects.
        """
        for extension in self.INPUT_FORMATS:
            found_music_file_paths = list(inputdir.rglob('*{}'.format(extension)))
            found_music_files = [MusicFile(path) for path in found_music_file_paths]
            self.files.extend(found_music_files)
    
    def convertAll(self, sourceRoot, destRoot, bitrate):
        """
        Convert all files in self.files to mp3 format and write them to outputdir.
        """
        for music_file in self.files:
            # Create absolute path to output file
            sourceRelativePath = os.path.relpath(music_file.filepath,sourceRoot)
            sourceRelativePath = os.path.splitext(sourceRelativePath)[0] + '.mp3'
            destFullPath = os.path.join(destRoot,sourceRelativePath)

            if os.path.exists(destFullPath):
                logger.info('Skipping {} because it already exists'.format(destFullPath))
                continue

            if not os.path.exists(os.path.dirname(destFullPath)):
                os.makedirs(os.path.dirname(destFullPath))

            if music_file.filepath.suffix == '.mp3':
                logger.info('Copying existing MP3 {}'.format(destFullPath))
                shutil.copyfile(music_file.filepath, destFullPath)
            else:
                convert_to_mp3(music_file.filepath, destFullPath, bitrate)