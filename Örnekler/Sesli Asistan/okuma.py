from gtts import gTTS
import os

def speak(okuncak):
    print(okuncak)
    tts = gTTS(text=okuncak, lang='tr')
    tts.save("ses.mp3")
    os.system("ses.mp3")
