boy=float(input("Boyunuzu Giriniz (Metre Cinsinden): "))
kg=float(input("Kilonuzu Giriniz: "))

vki=kg/(boy*boy)

if vki<18:
    print("Vücut Kitle İndeksiniz {} Zayıfsınız".format(vki))
elif 18<vki<25:
    print("Vücut Kitle İndeksiniz {} Normalsiniz".format(vki))
elif 25<vki<30:
    print("Vücut Kitle İndeksiniz {} Kilolusunuz".format(vki))
elif 30<vki<34:
    print("Vücut Kitle İndeksiniz {} Obezsiniz".format(vki))
elif vki>35:
    print("Vücut Kitle İndeksiniz {} Ciddi Obezsiniz".format(vki))
