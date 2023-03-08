not1=int(input("Birinci Notu Giriniz: "))
not2=int(input("İkinci Notu Giriniz: "))
not3=int(input("Üçüncü Notu Giriniz: "))

ortalama=(not1+not2+not3)/3

if ortalama>=50:
    print("Ortalamanız ",ortalama," Geçtiniz")

else:
    print("Ortalamanız ",ortalama," Kaldınız")
