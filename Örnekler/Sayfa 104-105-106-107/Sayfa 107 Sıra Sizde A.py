sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))

toplam=0
for sayilar in range(sayi1,sayi2):
    toplam=toplam+sayilar
print("2 Sayı Arasındaki Sayıların Toplamı ",toplam)
