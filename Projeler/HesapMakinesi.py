def toplama(sayi1,sayi2):
    return sayi1+sayi2

def cıkarma(sayi1,sayi2):
    return sayi1-sayi2

def bolme(sayi1,sayi2):
    return sayi1/sayi2

def carpma(sayi1,sayi2):
    return sayi1*sayi2

print("Hesap Makinesi")

print("\n  Toplama: 1  Çıkarma: 2  \n  Çarpma: 3   Bölme: 4 \n        Çıkış: q \n\n")

while True:
    islem=str(input("Yapmak İstediğiniz işlemi Seçiniz: "))
    if islem=="q":
        break

    sayi1=int(input("1. Sayıyı Griniz: "))
    sayi2=int(input("2. Sayıyı Giriniz: "))


    if islem=="1":
        print("2 Sayıyı Topladım Sonuç ",toplama(sayi1,sayi2))

    elif islem=="2":
        print("2 Sayıyı Çıkardım Sonuç ",cıkarma(sayi1,sayi2))

    elif islem=="3":
        print("2 Sayıyı Çarptım Sonuç ",carpma(sayi1,sayi2))

    elif islem=="4":
        print("1. Sayıyı 2. Sayıya Böldüm Sonuç ",bolme(sayi1,sayi2))
    else:
        print("Yanlış Seçim Yaptınız Tekrar Deneyiniz")
