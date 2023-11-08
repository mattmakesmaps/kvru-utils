import logging
from pydub import AudioSegment
from pydub.utils import mediainfo

def convert_to_mp3(infile, outfile, bitrate):
    try:
        metadata = mediainfo(infile)
        infileHandle = AudioSegment.from_file(infile)
        infileHandle.export(outfile, format='mp3', bitrate=bitrate, tags=metadata['TAG'])
        logging.info('Converted {}'.format(outfile))
    except Exception as e:
        logging.error('Failed to convert {}'.format(infile))
        logging.error(e)
        return False

    return True
