while True:
    sifre=input("8 Karakterlik Bir Şifre Giriniz: ")
    karakter_sayisi=len(sifre)
    if karakter_sayisi<8:
        print("Şifreniz 8 Karakter Olmalıdır")
    if karakter_sayisi>=8:
        print("Şifreniz Kaydedildi")
    break
