sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayac=0


for x in range(0,len(sayilar)):
    sayi=sayilar[x]
    if sayi%2==0:
        sayac+=1
        print("Listedeki {}. Çift Sayı {}".format(sayac,sayi))
