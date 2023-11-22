import argparse
import logging
import os
import pathlib

from datetime import datetime

from mp3convertpackage import Ledger

if __name__ == "__main__":
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
        "-l",
        "--logdir",
        type=str,
        help="Specify dir for logfiles. Two are created, one containing checksums and another containing stdout messages. Defaults to parent dir of this script. ",
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
    LOGPATH = os.path.dirname(os.path.realpath(__file__)) + "/mp3convert.log"
    CHECKSUM_CSV_PATH = os.path.dirname(os.path.realpath(__file__)) + "/mp3convert-checksums.log"

    logger = logging.getLogger("mp3convert")
    logger.setLevel(logging.INFO)
    loggerFileHandler = logging.FileHandler(LOGPATH)
    loggerConsoleHandler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    loggerFileHandler.setFormatter(formatter)
    loggerConsoleHandler.setFormatter(formatter)
    logger.addHandler(loggerFileHandler)
    logger.addHandler(loggerConsoleHandler)

    logger.info("Run Beginning. Input: %s, Output: %s", INPUT_DIR, OUTPUT_DIR)
    starttime = datetime.now()

    ledger = Ledger(INPUT_DIR, OUTPUT_DIR, CHECKSUM_CSV_PATH)
    ledger.search_for_files()

    logger.info("Found %d files in %s", len(ledger.files), INPUT_DIR)

    if not args.dry_run:
        ledger.convert_all(args.bitrate)

    elapsedtime = datetime.now() - starttime
    logger.info("Run Complete: Total Time: %s", elapsedtime)
