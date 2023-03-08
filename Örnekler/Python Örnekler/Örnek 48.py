sayi=input("Rakamları Çarpılcak Sayı Giriniz: ")
sonuc=1

for x in sayi:
    if not int(x)==0:
        sonuc*=int(x)

print("{} Sayısının Rakamlarını Çarptım Sonuç {}".format(sayi,sonuc))
