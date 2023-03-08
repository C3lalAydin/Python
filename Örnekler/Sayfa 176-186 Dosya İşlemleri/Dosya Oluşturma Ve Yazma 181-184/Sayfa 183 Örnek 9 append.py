import os
import datetime
os.chdir("C:\\test")

dosya=open("tarih.txt","w")
tarih=datetime.date.today()  #Bugün nün Tarihi
dosya.write(str(tarih)+"\n")  #Tarih verisini stringe dönüştürüp bi alt satıra geçiyor
dosya.close() #Dosyayı kapatıyor

dosya=open("tarih.txt")
print(dosya.read())
dosya.close() #Dosyayı kapatıyor

dosya=open("tarih.txt","a")
saat=datetime.datetime.now().time()  #Şuanki Saat
dosya.write(str(saat)+"\n") #Saat verisini stringe dönüştürüp bi alt satıra geçiyor
dosya.close() #Dosyayı kapatıyor

dosya=open("tarih.txt")
print(dosya.read())
dosya.close() #Dosyayı kapatıyor

"""
Kod Bloğunda Yeni Bir Dosya oluşturulmuş İçeriğine tarih bilgisi içeren bir satır eklenmiştir.
Daha sonra düzenlemek için açılan dosya ya saat bilgisi eklenmiş ve dosya okunup ekrana yazılmıştır.
"""
