def yildiz_ucgen_ciz():
    print("Yıldız Üçgen Çiziliyor:")
    for ucgen_sayisi in range(1,5+1):
        print(("*"*ucgen_sayisi)+(" "*(5-ucgen_sayisi))+(" "*(5-ucgen_sayisi))+("*"*ucgen_sayisi))
    for ucgen_sayisi in range(5,1-1,-1):
        print(("*"*ucgen_sayisi)+(" "*(5-ucgen_sayisi))+(" "*(5-ucgen_sayisi))+("*"*ucgen_sayisi))




yildiz_ucgen_ciz()
