import os,shutil
os.chdir("C:\\test")

yedek_dizini=os.path.join("C:\\","test","Yedek")
dosya="tarih.txt"

if os.path.exists(yedek_dizini):
    print("Yedek Dizini Var ",yedek_dizini)
    if os.path.isdir(yedek_dizini):
        print("Bu Bir Dizin ",yedek_dizini)
else:
    print("Yedek Dizini Bulunamadı")
    os.mkdir(yedek_dizini)
    print("Oluşturuluyor...")

yedek_dosya=os.path.join(yedek_dizini,"tarih_yedek.txt")

if os.path.exists(dosya):
    print("Dosya Mevcut Yedekleniyor")
    shutil.copy(dosya,yedek_dosya)

if os.path.exists(yedek_dosya):
    print("Dosya Başarı İle Yedeklendi")
