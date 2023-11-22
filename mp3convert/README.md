# mp3-convert

Convert a source directory of WAV/AIFF/MP3 files to MP3 format.

Relies on [pydub](https://github.com/jiaaro/pydub) and `ffmpeg` for conversion.

Install via `pipenv`:

`pipenv install --dev`

Run via `pipenv`:

`pipenv run python ./mp3-convert.py --help`

Run Tests:

`pipenv run pytest`

## Notes

- Default behavior is to copy the directory structure of `inputdir` to `outputdir`
- Default `--bitrate` is `192K`.
- MP3 files in `inputdir` are copied to `outputdir` no bitrate change is applied.