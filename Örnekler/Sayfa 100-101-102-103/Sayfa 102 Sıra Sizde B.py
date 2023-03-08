kac_saat=int(input("Otoparkı Kaç Saat Kullandınız: "))



if kac_saat==1:
    print(kac_saat," Saat İçin ",kac_saat*5," TL Ödeyiniz")

elif kac_saat<=5:
    print(kac_saat," Saat İçin ",kac_saat*4," TL Ödeyiniz")

elif kac_saat>=5:
    print(kac_saat," Saat İçin ",kac_saat*3," TL Ödeyiniz")

