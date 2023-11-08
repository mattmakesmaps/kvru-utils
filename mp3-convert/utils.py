"""Utility methods that don't fit into a specific class."""
import logging
from pydub import AudioSegment
from pydub.utils import mediainfo

logger = logging.getLogger("mp3-convert.utils")


def convert_to_mp3(infile, outfile, bitrate):
    """
    Convert an audio file to mp3 format.

    If an error is encountered, log it but do not raise an exception.
    """
    try:
        metadata = mediainfo(infile)
        infile_handle = AudioSegment.from_file(infile)
        infile_handle.export(
            outfile, format="mp3", bitrate=bitrate, tags=metadata["TAG"]
        )
        logger.info("Converted %s", outfile)
    except Exception as e:
        logger.error("Failed to convert %s", infile)
        logger.error(e)
        return False

    return True
