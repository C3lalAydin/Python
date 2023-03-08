import os
yol=os.path.join("C:\\","test","tarih.txt")
if os.path.exists(yol):  #esists() Yolun Var olup  Olmadığını Kontrol Eder
    print(yol+" : konumu var")
    if os.path.isfile(yol):   #isfile() Erişilen Konumunun Dosya Olup Olmadığını Kontrol Eder
        print(yol+" : Bu Bir Dosya")
    else:
        print("Bu Bir Dosya Değil")
else:
    print("Yol Bulunamadı")
