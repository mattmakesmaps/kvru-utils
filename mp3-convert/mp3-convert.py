import argparse
import logging
import os
import pathlib

from datetime import datetime

from Ledger import Ledger

if __name__ == '__main__':
    logpath = os.path.dirname(os.path.realpath(__file__)) + '/mp3-convert.log'
    logging.basicConfig(filename=logpath,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    parser = argparse.ArgumentParser(description='Convert audio files to mp3 format.')
    parser.add_argument('inputdir')
    parser.add_argument('outputdir')
    parser.add_argument('-b', '--bitrate', type=str, default='192k', help='Bitrate of the output wav files')
    parser.add_argument('--flat', action='store_true', help='Do not preserve directory structure')
    parser.add_argument('--dry-run', action='store_true', help='Do not actually convert files')
    args = parser.parse_args()

    INPUT_DIR = pathlib.Path(args.inputdir)
    OUTPUT_DIR = pathlib.Path(args.outputdir)


    logging.info('Run Beginning. Input: {}, Output: {}'.format(INPUT_DIR, OUTPUT_DIR))
    starttime = datetime.now()

    ledger = Ledger()
    ledger.searchForFiles(INPUT_DIR)

    logging.info('Found {} files in {}'.format(len(ledger.files), INPUT_DIR))

    if not args.dry_run:
        ledger.convertAll(INPUT_DIR, OUTPUT_DIR, args.bitrate)

    elapsedtime = datetime.now() - starttime
    logging.info('Run Complete: Total Time: {}'.format(elapsedtime))