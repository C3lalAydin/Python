from audioplayer import AudioPlayer
from gtts import gTTS
import os


while True:
    sor=input("Söylencek ve Kaydedilcek Metni Giriniz [Çıkmak için '0'a basınız]: ")
    if sor=="0":
        quit()
    try:
        ses = gTTS(sor,lang="tr")
        ses.save("ses.mp3")
        AudioPlayer("ses.mp3").play(block=True)
    except Exception as AssertionError:
        print("Lütfen Bir Değer Giriniz.")
