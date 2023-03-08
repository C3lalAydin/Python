ad=input("Adınızı Giriniz: ")
maas=int(input("Maaşınızı Giriniz: "))
calisma_yil=int(input("Kaç Yıldır Çalışıyorsunuz: "))



if  calisma_yil>0 and calisma_yil<=5:
    print("Sayın ",ad," Zamlı Maaşınız ",maas+((maas*10)/100)," TL")

elif  calisma_yil>5 and calisma_yil<=10:
    print("Sayın ",ad," Zamlı Maaşınız ",maas+((maas*15)/100)," TL")

elif  calisma_yil>=11:
    print("Sayın ",ad," Zamlı Maaşınız ",maas+((maas*25)/100)," TL")
    
