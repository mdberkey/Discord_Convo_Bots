from gtts import gTTS


# returns tts file of text
def TTSus(text):
    tts = gTTS(text, lang='en-us')  # female english American accent
    tts.save("audio.mp3")


def TTSau(text):
    tts = gTTS(text, lang='en-au')  # female english Australian accent
    tts.save("audio.mp3")
