def tam_bölenleri_bul(sayi):
    tam_bölenler=[]

    for x in range(2,sayi):                  #Her sayı 1 e zaten bölündüğü için 2 ile başlanmıştır
        if sayi%x==0:
            tam_bölenler.append(x)
    return tam_bölenler


sor=int(input("Tam Bölenlerini Öğrenmek İstediğiniz Sayıyı Giriniz: "))

a=tam_bölenleri_bul(sor)


print("{} Sayısının Tam Bölenleri {}".format(sor,a))
