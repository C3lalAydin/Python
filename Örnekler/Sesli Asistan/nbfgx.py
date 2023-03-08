import time
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import urllib.request
import json
import requests
import webdriver
metin= ""
def Dark():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("dinlemedeyem")
        audio = r.listen(source)
        gelen = str(r.recognize_google(audio,language = "tr"))
        print("dediyiniz soz:"+gelen)
        bla = gelen.split()
        if "aç" in bla:
            youtube = webdriver.Chrome()
            youtube.get("https://www.youtube.com/results?search_query=" + gelen)
            youtube.find_element_by_xpath('//*[@id="video-title"]').click()
        elif "takipçi" in bla:
            name = "Kanal İD niz"
            key = "APİ Key"
            data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + name + "&key=" + key).read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            a = ("senin şu anda %d" % int(subs) + "takipçin var")
            print(a)
            tts = gTTS(text=a,lang="tr")
            subs = "subs.mp3"
            tts.save(subs)
            mixer.music.load(subs)
            mixer.music.play()
        elif "Dark"in bla:
            tts = gTTS(text="dinlemedeyim!",lang="tr")
            asistan = ("isimm.mp3")
            mixer.music.load(asistan)
            mixer.music.play()
        elif "tamam"in bla:
            print("Nasılsın")
        else:
            params = dict(
                username='Dark__',
                token='tokeninizi buraya yazın',
                code=metin,
                type='text'
            )
            cevap = json.loads(
                requests.post("http://beta.ceyd-a.com/jsonengine.jsp", data=params).content.decode('utf-8')[
                1:-3]).get("answer")
            tts = gTTS(text=cevap,lang="tr")
            ceyda = str(("isim.mp3"))
            tts.save(ceyda)
            mixer.music.load(ceyda)
            mixer.music.play()
while True:
    Dark()
