from datetime import datetime

bugun=datetime.today()
print("Bugünün Tarihi: {}".format(bugun))

yil=int(input("Hangi Yılda Doğdunuz: "))
ay=int(input("Kaçıncı Ayda Doğduğunuzu Giriniz: "))
gun=int(input("Doğduğunuz Günü Giriniz: "))

dogum_gunum=datetime(year=yil,month=ay,day=gun)
yas=bugun-dogum_gunum

print("{} Gün Önce Doğdunuz".format(yas.days))


#print(yas.days)  Sadece Günü Yazdırır
#print(yas.seconds)  Sadece Saniyeyi Yazdırır
#print(yas.microseconds)  Sadece Mikrosaniyeyi Yazdırır
#print(yas)       Hepsini Yazdırır
