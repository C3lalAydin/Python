sayi1=int(input("Birinci Sayıyı Giriniz: "))
sayi2=int(input("İkinci Sayıyı Giriniz: "))
sayi3=int(input("Üçüncü Sayıyı Giriniz: "))

if sayi1>sayi2 and sayi1>sayi3:
    print(sayi1,",",sayi2," ve ",sayi3," Arasından En Büyük Sayı ",sayi1)

elif sayi2>sayi1 and sayi2>sayi3:
    print(sayi1,",",sayi2," ve ",sayi3," Arasından En Büyük Sayı ",sayi2)

elif sayi3>sayi2 and sayi3>sayi1:
    print(sayi1,",",sayi2," ve ",sayi3," Arasından En Büyük Sayı ",sayi3)
