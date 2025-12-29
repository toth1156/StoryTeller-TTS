class VoiceRegistry:
    def __init__(self):
        self.assigned={}
        self.male=["male_1","male_2"]
        self.female=["female_1","female_2"]
    def get_voice(self,speaker,hint):
        if speaker in self.assigned:
            return self.assigned[speaker]
        voice=(self.female if "female" in hint.lower() else self.male).pop(0)
        self.assigned[speaker]=voice
        return voice
