sor=input("Sinemamı Tiyatromu (Sinema/Tiyatro): ")
ogrenci=input("Öğrencimisiniz (E/H): ")

if sor=="Sinema" and ogrenci=="E":
    print("Sinemaya Girmek İçin Vereceğiniz Tutar ",15-((15*50)/100)," TL")

elif sor=="Sinema" and ogrenci=="H":
    print("Sinemaya Girmek İçin Vereceğiniz Tutar ",15," TL")

elif sor=="Tiyatro" and ogrenci=="E":
    print("Tiyatroya Girmek İçin Vereceğiniz Tutar ",10-((10*50)/100)," TL")

elif sor=="Tiyatro" and ogrenci=="H":
    print("Tiyatroya Girmek İçin Vereceğiniz Tutar ",10," TL")

