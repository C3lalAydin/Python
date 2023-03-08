sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))

toplam=0


while sayi1<sayi2:   #2 Sayının Arasındaki Sayısı İstoyrsa (Sondaki Dahil Değil) O zaman Sadedce "<" Koymalıyız. Sondaki Sayı Dağilse "<=" Koymalıyız
    toplam+=sayi1
    sayi1+=1
print(toplam)
