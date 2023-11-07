from simple_file_checksum import get_checksum

class MusicFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self._checksum = get_checksum(self.filepath, algorithm='md5')

    @property
    def checksum(self):
        return self._checksum
