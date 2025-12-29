import os
from openai import OpenAI
client=OpenAI()
def generate_voice(text,speaker,voice,index,output_dir):
    os.makedirs(output_dir,exist_ok=True)
    path=f"{output_dir}/{index:03d}_{speaker}.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",voice=voice,input=text) as r:
        r.stream_to_file(path)
    return path
