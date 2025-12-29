import os
def generate_voice(text,speaker,voice,index,output_dir):
    os.makedirs(output_dir,exist_ok=True)
    path=f"{output_dir}/{index:03d}_{speaker}.wav"
    open(path,"wb").close()
    return path
