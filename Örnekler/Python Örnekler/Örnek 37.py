sayi=int(input("Kaç Adet Sayı Girilcek: "))

teksayac=0
ciftsayac=0
tektoplam=0
cifttoplam=0


for x in range(1,sayi+1):
    gir=int(input("{}. Sayıyı Giriniz: ".format(x)))
    if gir%2==0:
        ciftsayac+=1
        cifttoplam+=gir
    elif not x%2==0:
        teksayac+=1
        tektoplam+=gir

ortalama_tek=tektoplam/teksayac
ortalama_cift=cifttoplam/ciftsayac


print("Tek Sayıların Ortalaması: {}".format(int(ortalama_tek)))
print("Çift Sayıların Ortalaması: {}".format(int(ortalama_cift)))
