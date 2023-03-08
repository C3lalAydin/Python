def selamla():   #selamla() fonskiyonunu oluşturuyoruz.
    ad=str(input("Adınızı giriniz: "))
    if ad:                                #Ad değişkeni girlirse çalışır
        print("Merhaba {}".format(ad))
    else:                                #Ad değişkeni Doldurulmazsa Çalışır
        print("Merhaba Arkadaşlar !")
selamla()
