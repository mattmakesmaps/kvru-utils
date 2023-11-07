import argparse
from Ledger import Ledger
from utils import convert_to_mp3


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert audio files to mp3 format.')
    parser.add_argument('inputdir')
    parser.add_argument('outputdir')
    parser.add_argument('-b', '--bitrate', type=str, default='192k', help='Bitrate of the output wav files')
    parser.add_argument('--flat', action='store_true', help='Do not preserve directory structure')
    parser.add_argument('--dry-run', action='store_true', help='Do not actually convert files')
    parser.add_argument('--verbose', action='store_true', help='Print verbose output')
    args = parser.parse_args()

    INPUT_DIR = args.inputdir
    OUTPUT_DIR = args.outputdir

    ledger = Ledger()
    ledger.searchForFiles(INPUT_DIR)

    convert_to_mp3(ledger.files[0].filepath, '/home/matt/Desktop/test2.mp3', args.bitrate)