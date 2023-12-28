import pathlib

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from pydub.utils import mediainfo

"""
Restructure metadata tags for import into libretime.

pydub.utils.mediainfo() is used to read tags from the file.
mutagen is used to write tags.

We're doing this because the `EasyID3` class in mutagen hides
all the non-standard tags that are cleanly represented by mediainfo().
"""


def getTrackTitle(sourceMetadata):
    """
    Return track title in order of preference based on research
    found in `tag_exploration.ipynb
    """
    if 'tttl' in sourceMetadata:
        return sourceMetadata['tttl']
    
    if 'comment' in sourceMetadata:
        return sourceMetadata['comment']

    if 'title' in sourceMetadata:
        return sourceMetadata['title']
    
    return None

def getAlbum(sourceMetadata):
    if 'IALB' in sourceMetadata:
        return sourceMetadata['IALB']
    return None

def getGenre(sourceMetadata):
    if 'IGRE' in sourceMetadata:
        return sourceMetadata['IGRE']
    return None

if __name__ == "__main__":
    # Get metadata from file.
    MP3_ROOT_DIR = pathlib.Path("/Users/matthewkenny/projects/kvru-utils/mp3convert/prod/dest/")

    mp3_paths = list(MP3_ROOT_DIR.rglob("*.mp3"))
    print("Found {} mp3 files.".format(len(mp3_paths)))

    num_files_processed = 0

    for mp3_file in mp3_paths:
        if num_files_processed % 100 == 0:
            print("Processed {} files.".format(num_files_processed))

        metadata = mediainfo(mp3_file)

        # skip files without metadata.
        if 'TAG' not in metadata:
            num_files_processed += 1
            continue

        source_title = getTrackTitle(metadata['TAG'])
        source_album = getAlbum(metadata['TAG'])
        source_genre = getGenre(metadata['TAG'])

        # Write metadata back in correct tags.
        audio = MP3(mp3_file, ID3=EasyID3)

        # Only update if it's not already set and we have found a good value.
        if 'title' not in audio and source_title:
            audio['title'] = source_title 
        
        if 'album' not in audio and source_album:
            audio['album'] = source_album
        
        if 'genre' not in audio and source_genre:
            audio['genre'] = source_genre
        
        audio.save()
        num_files_processed += 1