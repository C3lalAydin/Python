sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))

if sayi1>sayi2:
    sayi=sayi1-sayi2
else:
    sayi=sayi2-sayi1


toplam=0
for sayilar in range(sayi1,sayi2):
    toplam=toplam+sayilar

ortalama=toplam/sayi
print("2 Sayının Arasındaki Sayıların Ortalaması ",ortalama)
