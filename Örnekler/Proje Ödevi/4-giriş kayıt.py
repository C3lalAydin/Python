adlar=[]
okul_nolar=[]
giris=int(input("Giriş Yapmak İçin(1)e Basın: "))
if giris==1:
    ad=(input("Adınızı Giriniz: "))
    okul_no=(input("Okul Numaranızı Giriniz: "))
if (ad in adlar) and (okul_no in okul_nolar):
    print("Giriş Yaptınız")
else:
    print("Giriş Yapamadınız,Kayıtlı Değilsiniz")
    kayit=str(input("\nKayıt Olmak İçin(3)e Basın: "))

if kayit=="3":
    kayit_ad=(input("\nKayıt Olmak İçin Adınızı Girin: "))
    kayit_okulno=(input("Kayıt Olmak İçin Okul Numaranızı Girin: "))

adlar.append(kayit_ad)
okul_nolar.append(kayit_okulno)


giris2=int(input("\n\nTekrar Giriş Yapmak İsterseniz(1)e Basın: "))
if giris2==1:
    ad=(input("Adınızı Giriniz: "))
    okul_no=(input("Okul Numaranızı Giriniz: "))
if (ad in adlar) and (okul_no in okul_nolar):
    print("\nGiriş Yaptınız")
else:
    print("\nGiriş Yapamadınız")
