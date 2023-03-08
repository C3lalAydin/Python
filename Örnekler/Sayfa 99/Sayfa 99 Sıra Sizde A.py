sinav_not1=int(input("Birinci Sınav Notunuzu Giriniz: "))
sinav_not2=int(input("İkinci Sınav Notunuzu Giriniz: "))
performans_not=int(input("Performans Notunuzu Giriniz: "))

ortalama=(sinav_not1+sinav_not2+performans_not)/3

if ortalama>=50:
    print("Başarılı")
else:
    print("Başarısız")
