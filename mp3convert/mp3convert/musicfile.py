import os
from simple_file_checksum import get_checksum


class MusicFile:
    """Represents an individual source audio file."""
    def __init__(self, filepath):
        self.filepath = filepath
        self._checksum = get_checksum(self.filepath, algorithm='md5')

    @property
    def checksum(self):
        return self._checksum
    
    def generate_relative_path(self, root):
        """
        Generate a relative path to this file from a given root directory.
        """
        return os.path.relpath(self.filepath, root)