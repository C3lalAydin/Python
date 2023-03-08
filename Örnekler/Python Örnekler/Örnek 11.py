try:
    yas=int(input("Yaşınızı Giriniz: "))
    if yas>=18:
        print("Ehliyet Alabilirsiniz")
    elif 1<=yas<18:
        print("Ehliyet Alamazsınız Yaşınız Tutmuyor")
    elif yas==0:
        print("0 Yaşında Olduğuna Eminmisin")
    elif yas<0:
        print("Yaşınız 0 dan Küçüksünüz. Daha Doğmadınız Galiba")

except ValueError:
    print("Lütfen Harf ve Float Sayı Girmeyiniz. Tam Sayı Giriniz")
