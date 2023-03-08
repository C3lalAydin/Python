urun1=int(input("Birinci Ürünün Fiyatını Giriniz: "))
urun2=int(input("İkinci Ürünün Fiyatını Giriniz: "))

toplam=urun1+urun2

if toplam<=200:
    print("Ödenecek Miktar ",toplam," TL")

if toplam>=201:
    indirim=(toplam*25)/100
    sonuc=toplam-indirim
    print("Ödenecek Miktar,İndirimden Sonra ",sonuc," TL")
