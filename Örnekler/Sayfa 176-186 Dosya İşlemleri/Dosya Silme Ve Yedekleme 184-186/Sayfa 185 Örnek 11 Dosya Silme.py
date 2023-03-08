import os
os.chdir("C:\\test")

if os.path.exists("tarih.txt"):
    print("Dosya Mevcut Siliniyor....")
    os.remove("tarih.txt")    #Yazılan Dosyayı Siler
else:
    print("Bu Dosya Mevcut Değil")
