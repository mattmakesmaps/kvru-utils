from pydub import AudioSegment

def convert_to_mp3(infile, outfile, bitrate):
    AudioSegment.from_file(infile).export(outfile, format='mp3', bitrate=bitrate)
    return True
