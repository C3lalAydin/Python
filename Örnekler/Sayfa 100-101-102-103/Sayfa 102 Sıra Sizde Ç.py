boy=float(input("Boyunuzu(Metre Cinsinden) Giriniz: "))
agırlık=int(input("Kilonuzu Giriniz: "))

vki=agırlık/(boy*boy)

if vki>=18 and vki<25:
    print("Vücud Kitle İndeksiniz ",vki,",Durumunuz Normal")

elif vki>=25 and vki<30:
    print("Vücud Kitle İndeksiniz ",vki,",Kilolusunuz")

elif vki>=30 and vki<35:
    print("Vücud Kitle İndeksiniz ",vki,",Obezsiniz")

elif vki>=35:
    print("Vücud Kitle İndeksiniz ",vki,",Ciddi Obezsiniz")

