try:
    ortalamasi=int(input("Yazılı Ortalamanızı Giriniz: "))

    if ortalamasi>100:
        print("Lütfen 100 den Küçük Bir Sayı Giriniz")
    elif ortalamasi>=50:
        print("Ortalamanız {} Sınıfı Geçtiniz".format(ortalamasi))
    elif ortalamasi>100:
        print("Lütfen 100 den Küçük Bir Sayı Giriniz")
    elif ortalamasi<=0:
        print("Lütfen 0 dan Büyük Bir Sayı Giriniz")
    elif ortalamasi<50:
        print("Ortalamanız {} Sınıfta Kaldınız".format(ortalamasi))

except ValueError:
    print("Lüften Harf Yada Float Sayı Girmeyiniz. Tam Sayı Giriniz")
