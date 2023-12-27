# mp3-convert

Convert a source directory of WAV/AIFF/MP3 files to MP3 format.

Relies on [pydub](https://github.com/jiaaro/pydub) and `ffmpeg` for conversion.

**Install via `pipenv`:**

`pipenv install --dev`

**Run via `pipenv`:**

`pipenv run python ./mp3-convert.py --help`

**Run Tests:**

from `./mp3convert/tests/` run `pipenv run python -m unittest`

- Use `foobar2000` to edit metadata for test files.

## Notes

- Default behavior is to copy the directory structure of `inputdir` to `outputdir`
- Default `--bitrate` is `192K`.
- MP3 files in `inputdir` are copied to `outputdir` no bitrate change is applied.

## Usage Output

```
usage: mp3convert.py [-h] [-b BITRATE] [-l LOGDIR] [--separate-missing-metadata] [--dry-run] inputdir outputdir

Convert audio files to mp3 format.

positional arguments:
  inputdir
  outputdir

options:
  -h, --help            show this help message and exit
  -b BITRATE, --bitrate BITRATE
                        Bitrate of the output wav files
  -l LOGDIR, --logdir LOGDIR
                        Specify dir for logfiles. Two are created, one containing checksums and 
                        another containing stdout messages. Defaults to parent dir of this script.
  --separate-missing-metadata
                        Create two subdirs in outputdir, one for files with metadata and one 
                        for files without metadata.
  --dry-run             Do not actually convert files
```