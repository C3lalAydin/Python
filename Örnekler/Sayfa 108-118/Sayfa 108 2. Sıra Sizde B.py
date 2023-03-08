sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]
sayilar.extend(sayilar2)    #Listeleri Birleştirir Sayilar2 listesindeki elemanları sayilar listesine ekler

for x in sayilar:
    if x%4==0:              # X 4 e tam Bölünüyorsa Ekrana Yazdır
        print("{} Sayısı 4'e Tam Bölünüyor".format(x))
