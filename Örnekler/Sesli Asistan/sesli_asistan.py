#Kütüphanelerimizi Tanımlıyoruz.
import speech_recognition as sr
import time
import datetime
import os
from okuma import speak
from hava import hava
import feedparser


try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)
        metin = str(r.recognize_google(audio,language = "tr"))
        print("Dediğiniz Söz:"+metin)
        bla=metin.split()


        bugun=datetime.datetime.today()
        saat="Saat "+bugun.strftime("%X")
        if "saat" in bla:
            speak(saat)

        if "nasılsın" in bla:
            speak("İyiyim Sen Nasılsın")
        if "aç" in bla:
            metin2=metin.split()
            print(metin2)
            os.startfile("https://www.youtube.com/results?search_query=" + metin2[1])

        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|07060|ANTALYA|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        if "hava" in bla:
            hava1=str(parse[2]+parse[4]+parse[5])
            speak(hava1)

        os.remove("ses.mp3")
except sr.UnknownValueError:
    print("Anlayamadım")
