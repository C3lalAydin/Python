sor1=str(input("Sinemamı Tiyatromu [sinema/tiyatro]: "))
sor2=str(input("Öğrencimisiniz [E/H]: "))

sinema=15
tiyatro=10

if sor2=="E":
    sinema=sinema/2
    tiyatro=tiyatro/2


if sor1=="sinema":
    print("Sinema İçin Verceğiniz Tutar {} TL".format(sinema))
elif sor1=="tiyatro":
    print("Tiyatro İçin Verceğiniz Tutar {} TL".format(tiyatro))
