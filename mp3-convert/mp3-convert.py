import argparse
import logging
import os
import pathlib

from datetime import datetime

from ledger import Ledger

if __name__ == "__main__":
    logger = logging.getLogger("mp3-convert")
    logger.setLevel(logging.INFO)
    logpath = os.path.dirname(os.path.realpath(__file__)) + "/mp3-convert.log"
    loggerFileHandler = logging.FileHandler(logpath)
    loggerConsoleHandler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    loggerFileHandler.setFormatter(formatter)
    loggerConsoleHandler.setFormatter(formatter)
    logger.addHandler(loggerFileHandler)
    logger.addHandler(loggerConsoleHandler)

    parser = argparse.ArgumentParser(description="Convert audio files to mp3 format.")
    parser.add_argument("inputdir")
    parser.add_argument("outputdir")
    parser.add_argument(
        "-b",
        "--bitrate",
        type=str,
        default="192k",
        help="Bitrate of the output wav files",
    )
    parser.add_argument(
        "--flat", action="store_true", help="Do not preserve directory structure"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Do not actually convert files"
    )
    args = parser.parse_args()

    INPUT_DIR = pathlib.Path(args.inputdir)
    OUTPUT_DIR = pathlib.Path(args.outputdir)

    logger.info("Run Beginning. Input: %s, Output: %s", INPUT_DIR, OUTPUT_DIR)
    starttime = datetime.now()

    ledger = Ledger()
    ledger.search_for_files(INPUT_DIR)

    logger.info("Found %d files in %s", len(ledger.files), INPUT_DIR)

    if not args.dry_run:
        ledger.convert_all(INPUT_DIR, OUTPUT_DIR, args.bitrate)

    elapsedtime = datetime.now() - starttime
    logger.info("Run Complete: Total Time: %s", elapsedtime)
