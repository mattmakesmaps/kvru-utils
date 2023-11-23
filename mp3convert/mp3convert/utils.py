"""Utility methods that don't fit into a specific class."""
import logging
from pydub import AudioSegment
from pydub.utils import mediainfo

logger = logging.getLogger("mp3convert.utils")

def has_metadata(infile):
    """
    Check if an audio file has metadata.

    Return True if metadata is present, False if not.
    """
    metadata = mediainfo(infile)
    if "TAG" in metadata:
        return True
    else:
        return False

def convert_to_mp3(infile, outfile, bitrate):
    """
    Convert an audio file to mp3 format.

    If an error is encountered, log it but do not raise an exception.
    """
    try:
        metadata = mediainfo(infile)
        infile_handle = AudioSegment.from_file(infile)

        # Include metadata if present in source file.
        if "TAG" in metadata:
            infile_handle.export(
                outfile, format="mp3", bitrate=bitrate, tags=metadata["TAG"]
            )
        else:
            infile_handle.export(
                outfile, format="mp3", bitrate=bitrate
            )

        logger.info("Converted %s", outfile)
    except Exception as e:
        logger.error("Failed to convert %s", infile)
        logger.error(e)
        return False

    return True
