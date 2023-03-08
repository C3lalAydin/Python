from datetime import datetime

bugun=datetime.today()

print("Bugün: ",bugun)
print("Haftanın Kaçıncı Günü: ",bugun.weekday())    #Haftanın Kaçıncı Günü - Pazartesi 0 , Pazar 6 arası
print("Hangi Yıldayız: ",bugun.year)                #Yıl bilgisi
print("Kaçıncı Aydayız: ",bugun.month)                #Ay Bilgisi
print("Kaçıncı Gündeyiz: ",bugun.day)                 #Gün Bilgisi
print("Saat Kaç: ",bugun.hour)                      #Saat Bilgisi
print("Dakika Kaç: ",bugun.minute)                  #Dakika Bilgisi
print("Saniye Kaç: ",bugun.second)                  #Saniye Bilgisi
