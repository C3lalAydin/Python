toplam=0
sayi=0
dongu_sayisi=0

while sayi!=1:
    dongu_sayisi+=1
    sayi=int(input("Sayı Giriniz: "))
    toplam+=sayi
    print(dongu_sayisi)


ortalama=(toplam-1)/(dongu_sayisi-1)
print("Girilen Sayıların Ortalaması ",ortalama)
