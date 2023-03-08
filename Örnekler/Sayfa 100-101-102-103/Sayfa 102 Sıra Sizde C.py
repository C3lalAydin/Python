a_kenar=int(input("Birinci Kenarı Giriniz: "))
b_kenar=int(input("İkinci Kenarı Giriniz: "))
c_kenar=int(input("Üçüncü Kenarı Giriniz: "))

if a_kenar==b_kenar==c_kenar:
    print("Bu Bir Eşkenar Üçgen")

elif a_kenar==b_kenar or a_kenar==c_kenar or b_kenar==c_kenar:
    print("Bu Bir İkizkenar Üçgen")

else:
    print("Bu Bir Çeşit Kenar Üçgen")
