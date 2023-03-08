from audioplayer import AudioPlayer
from gtts import gTTS
import os


while True:
    sor=input("Söylencek Metni Giriniz [Çıkmak için '0'a basınız]: ")
    if sor=="0":
        quit()
    try:
        ses = gTTS(sor,lang="tr")
        ses.save("sess.mp3")
        AudioPlayer("sess.mp3").play(block=True)
        os.remove("sess.mp3")
    except Exception as AssertionError:
        print("Lütfen Bir Değer Giriniz.")
