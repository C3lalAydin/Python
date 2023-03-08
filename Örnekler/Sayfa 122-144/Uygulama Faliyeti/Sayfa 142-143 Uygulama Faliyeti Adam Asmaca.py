import random
kelime_listesi=["türkiye","antalya","bilişim","programlama","okul","ödev","deniz","telefon","bilgisayar","istanbul","denizli","kitap","sınıf"]

secili_kelime= random.choice(kelime_listesi)  #Kelime Listesinden Rastgele Bir Kelime Seçer
tahmin_sayisi=5   #Kullanıcının Tahmin Hakkı
harfler=[]   #Kullanıcığının Girdiği Harfleri Saklıcağımız Liste
x=len(secili_kelime)
z=list("_"*x)

print(" ".join(z),end="\n")
while tahmin_sayisi>0:
    harf=input("Bir Harf Giriniz: ")
    if harf in harfler:
        print("Lütfen Önce Kullandığınız Harfleri Tekrar Girmeyiniz")
        continue
    elif len(harf)>1:
        print("Sadece Tek Bir Harf Girebilirsiniz")
        continue
    elif harf not in secili_kelime:  #Girilen Harf Kelime İçinde Yoksa
        tahmin_sayisi-=1
        print("{} Harfi Kelimede Yok.{} Tane Tahmin Hakkınız Kaldı".format(harf,tahmin_sayisi))
else:
    for i in range(len(secili_kelime)):
        if harf==secili_kelime[i]:
            print("Doğru Tahmin")
            z[i]=harf
            harfler.append(harf)
        print(" ".join(z),end="\n")
        cevap=input("Kelimenin Tamamını Tahmin Etmek İstiyormusunuz ['e' veya 'h']: ")

        if cevap=="e":
            tahmin=input("Kelimeyi Tahmin Edebilirsiniz: ")
            if tahmin==secili_kelime:
                print("Tebrikler Bildiniz")
                break
            else:
                tahmin_sayisi-=1
                print("Yanlış Tahmin Ettiniz.{} Tane Tahmin Hakkınız Kaldı".format(tahmin_sayisi))
        if tahmin_sayisi==0:
            print("Tahmin Hakkınız Kalmadı. Kaybettiniz ")
            break
