def diktorgen_alan_hesaplama(genislik,yukseklik):
    alan=genislik*yukseklik
    print("Bu Dikdörtgenin Alanı {} Birim".format(alan))

kenar1=int(input("1. Kenarı Giriniz: "))
kenar2=int(input("2. Kenarı Giriniz: "))

diktorgen_alan_hesaplama(kenar1,kenar2)
