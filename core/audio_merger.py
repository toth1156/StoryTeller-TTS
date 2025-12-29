from pydub import AudioSegment
def merge_audio(files,output):
    audio=AudioSegment.empty()
    for f in files:
        audio+=AudioSegment.from_file(f)
    audio.export(output,format="mp3")
