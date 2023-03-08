maas=float(input("Maaşınızı Giriniz: "))
zam=int(input("Zam Oranını Giriniz (Yüzde cinsinden): "))

maas_zam=(maas*zam)/100
yeni_maas=maas_zam+maas

print("Önceki Maaşınız {} TL Zamlı Yeni Maaşınız {} TL ".format(int(maas),int(yeni_maas)))
