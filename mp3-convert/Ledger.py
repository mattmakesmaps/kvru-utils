import pathlib
from MusicFile import MusicFile

class Ledger:
    def __init__(self):
        self.files = []
        self.INPUT_FORMATS = ('.mp3', '.wav', '.aiff')

    def searchForFiles(self, directory):
        """
        Recursively search an input directory. Populate self.files with MusicFile objects.
        """
        searchPath = pathlib.Path(directory)
        for extension in self.INPUT_FORMATS:
            found_music_file_paths = list(searchPath.rglob('*{}'.format(extension)))
            found_music_files = [MusicFile(path) for path in found_music_file_paths]
            self.files.extend(found_music_files)
        
        return True