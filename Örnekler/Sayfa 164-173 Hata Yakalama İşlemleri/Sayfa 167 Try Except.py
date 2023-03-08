
try:       #Hata Oluşması Muhtemel Kod Bloğu
    sayi=int(input("Bir Sayı Giriniz: "))
    karesi=sayi*sayi
    print("Sayının Karesi: ",karesi)
except:   #Hata durumunda Yapılcak İşlem 
    print("Lütfen Sayı Girin")
