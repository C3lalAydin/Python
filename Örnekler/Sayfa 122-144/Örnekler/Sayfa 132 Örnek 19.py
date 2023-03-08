def ortalama_hesapla(sinav1,sinav2,sozlu):
    ortalama=(sinav1+sinav2+sozlu)/3       #ortalama hesaplanması
    return ortalama

sinav1=int(input("1. Sınav Notunu Giriniz: "))
sinav2=int(input("2. Sınav Notunu Giriniz: "))
sozlu=int(input("Sözlü Notunuzu Giriniz: "))



if (ortalama_hesapla(sinav1,sinav2,sozlu)<50):
    print("Dersten Kaldın")
else:
    print("Geçti")
