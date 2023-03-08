def yildiz_ucgen_ciz(satir_sayisi):
    print("{} Satırlık Yıldız Üçgen Çiziliyor".format(satir_sayisi))
    for satir in range(1,(satir_sayisi+1)):
        print("*"*satir)


satir_sor=int(input("Kaç Satırlık Yıldız Üçgen Çizilsin: "))


yildiz_ucgen_ciz(satir_sor)  #Üçgen Çizme Fonskiyonu 15 Satır Parametresi İle Çağrılıyor 
