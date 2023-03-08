sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]

sayilar.extend(sayilar2)
sayac=0

for x in range(1,len(sayilar)):
    if sayilar[x]%4==0:
        sayac+=1
        print("Listede 4 e Bölünen {}. Sayı: {}".format(sayac,sayilar[x]))
