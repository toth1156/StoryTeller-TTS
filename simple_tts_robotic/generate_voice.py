import pyttsx3,os
engine=pyttsx3.init()
def generate_voice(text,speaker,voice,index,output_dir):
    os.makedirs(output_dir,exist_ok=True)
    path=f"{output_dir}/{index:03d}_{speaker}.wav"
    engine.save_to_file(text,path)
    engine.runAndWait()
    return path
