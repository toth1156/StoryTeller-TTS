from config import *
from core.parser import parse_script
from core.voice_registry import VoiceRegistry
from core.audio_merger import merge_audio

if USE_LOCAL_TTS:
    from local_tts_voice_creator.generate_voice import generate_voice
elif USE_CLOUD_TTS:
    from cloud_tts_voice_creator.generate_voice import generate_voice
elif USE_SIMPLE_TTS:
    from simple_tts_robotic.generate_voice import generate_voice
else:
    raise Exception("No TTS backend enabled")

SCRIPT_PATH = "input/script.txt"
OUTPUT_DIR = "output/lines"

def main():
    lines = parse_script(SCRIPT_PATH)
    registry = VoiceRegistry()
    generated_files = []

    for idx, line in enumerate(lines, start=1):
        voice = registry.get_voice(line["speaker"], line["voice_hint"])
        output_file = generate_voice(
            text=line["text"],
            speaker=line["speaker"],
            voice=voice,
            index=idx,
            output_dir=OUTPUT_DIR
        )
        generated_files.append(output_file)

    if MERGE_AUDIO:
        merge_audio(generated_files, "output/final/full_story.mp3")

if __name__ == "__main__":
    main()
