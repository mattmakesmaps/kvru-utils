import argparse
import logging
import os
import pathlib

from Ledger import Ledger

if __name__ == '__main__':
    logpath = os.path.dirname(os.path.realpath(__file__)) + '/mp3-convert.log'
    logging.basicConfig(filename=logpath, level=logging.INFO)

    parser = argparse.ArgumentParser(description='Convert audio files to mp3 format.')
    parser.add_argument('inputdir')
    parser.add_argument('outputdir')
    parser.add_argument('-b', '--bitrate', type=str, default='192k', help='Bitrate of the output wav files')
    parser.add_argument('--flat', action='store_true', help='Do not preserve directory structure')
    parser.add_argument('--dry-run', action='store_true', help='Do not actually convert files')
    parser.add_argument('--verbose', action='store_true', help='Print verbose output')
    args = parser.parse_args()

    INPUT_DIR = pathlib.Path(args.inputdir)
    OUTPUT_DIR = pathlib.Path(args.outputdir)

    ledger = Ledger()
    ledger.searchForFiles(INPUT_DIR)

    logging.info('Found {} files in {}'.format(len(ledger.files), INPUT_DIR))

    ledger.convertAll(INPUT_DIR, OUTPUT_DIR, args.bitrate)
