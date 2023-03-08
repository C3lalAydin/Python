try:
    sayi=int(input("Sayi Giriniz: "))
    if sayi%2==0:
        print("Bu Sayı Çift Sayıdır")
    elif not sayi%2==0:
        print("Bu Sayı Tek Sayıdır")
except ValueError:
    print("Lüften Harf Yada Float Sayı Girmeyiniz. Tam Sayı Giriniz")
