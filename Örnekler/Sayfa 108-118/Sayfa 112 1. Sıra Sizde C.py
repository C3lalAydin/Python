sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))

ilk_sayi=sayi1
ikinci_sayi=sayi2
toplam=0
dongu_sayisi=0

while sayi1<sayi2:
    dongu_sayisi+=1
    toplam+=sayi1
    sayi1+=1

ortalama=(toplam)/dongu_sayisi
print("{} ile {} Arasındaki Sayıların Ortalaması {}".format(ilk_sayi,ikinci_sayi,ortalama))
