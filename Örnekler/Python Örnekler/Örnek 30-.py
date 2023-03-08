sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))
yeni_sayi2=sayi2+1
toplam=0
sayac=0


def cift(y):
    return y%2==0


for x in range(sayi1,yeni_sayi2):
        if cift(x):
            toplam+=x
            sayac+=1

ortalama=toplam/sayac
print(ortalama)
