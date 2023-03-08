sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))
sayi2+=1

toplam=0

for x in range(sayi1,sayi2):
    toplam+=x

print("2 Sayının Arasındaki Sayıların Toplamı ({} ve {}): {} Eder".format(sayi1,sayi2,toplam))
