def faktoriyel(sayi):
    sonuc=1
    sayi=int(input("Sayı Giriniz: "))

    for i in range(1,sayi+1):
        sonuc=i*sonuc
    print("{} Sayısının Faktoriyeli {}".format(sayi,sonuc))

faktoriyel(5)
