import re
def parse_script(path):
    entries=[]
    with open(path) as f:
        for line in f:
            m=re.match(r"(.*?)\s*\((.*?)\):\s*(.*)", line.strip())
            if m:
                speaker,voice_hint,text=m.groups()
                entries.append({"speaker":speaker,"voice_hint":voice_hint,"text":text})
    return entries
