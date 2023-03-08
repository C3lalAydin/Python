def karakter_kontrol(x,y):
    if y in x:
        print("{} Harfi Metinde Var".format(y))
    elif not y in x:
        print("{} Harfi Metinde Yok".format(y))




metin=input("Metin Giriniz: ")
arancak_harf=input("Arancak Harfi Giriniz: ")

karakter_kontrol(metin,arancak_harf)
