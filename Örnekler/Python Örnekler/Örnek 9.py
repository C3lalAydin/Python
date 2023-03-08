try:
    sayi=int(input("Sayı Giriniz: "))
    if sayi<0:
        print("Bu Sayı Negatif")
    elif sayi>0:
        print("Bu Sayı Pozitif")
    elif sayi==0:
        print("Bu Sayı 0 dır")
except ValueError:
    print("Lüften Harf Yada Float Sayı Girmeyiniz.")
