import logging
from pydub import AudioSegment
from pydub.utils import mediainfo

logger = logging.getLogger("mp3-convert.utils")


def convert_to_mp3(infile, outfile, bitrate):
    try:
        metadata = mediainfo(infile)
        infileHandle = AudioSegment.from_file(infile)
        infileHandle.export(
            outfile, format="mp3", bitrate=bitrate, tags=metadata["TAG"]
        )
        logger.info("Converted {}".format(outfile))
    except Exception as e:
        logger.error("Failed to convert {}".format(infile))
        logger.error(e)
        return False

    return True
