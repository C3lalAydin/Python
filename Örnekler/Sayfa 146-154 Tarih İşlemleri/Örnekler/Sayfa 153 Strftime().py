import datetime

an=datetime.datetime.now()

print(an.strftime("%Y"))    #Yıl
print(an.strftime("%X"))    #Saat
print(an.strftime("%d"))    #Gün - Ayın Kaçıncı Günü
print(an.strftime("%A"))    #Gün - İsim olarak
print(an.strftime("%B"))    #Ay - İsim Olarak
print(an.strftime("%a"))    #Kısaltılmış Gün İsmi
print(an.strftime("%w"))    #Sayı Olarak Haftanın Kaçıncı Günü
print(an.strftime("%m"))    #Sayı Olarak Ay (Tek Haneliyse Başına 0 Eklicek)
print(an.strftime("%-m"))   #Sayı Olarak Ay
print(an.strftime("%y"))    #Yıl - Son İki Rakam Olarak
print(an.strftime("%H"))    #Saat(24 Saatlik Format) 0 Eklenmiş Sayı
print(an.strftime("%-H"))   #Saat(24 Saatlik Format)
print(an.strftime("%I"))    #Saat(12 Saatlik Format) 0 Eklenmiş Sayı
print(an.strftime("%-I"))   #Saat(12 Saatlik Format)
print(an.strftime("%p"))    #AM/ÖÖ - PM/ÖS Bilgisi
print(an.strftime("%M"))    #Dakika - 0 Eklenmiş Sayı
print(an.strftime("%-M"))   #Dakika
print(an.strftime("%S"))    #Saniye - 0 Eklenmiş Sayı
print(an.strftime("%-S"))   #Saniye
print(an.strftime("%f"))    #Mikrosaniye - 0 Eklenmiş Sayı
print(an.strftime("%j"))    #Yılın Kaçıncı Günü
print(an.strftime("%U"))    #Yılın Kaçıncı Haftası(Pazar Gününden Başlayarak)
print(an.strftime("%W"))    #Yılın Kaçıncı Haftası(Pazartesi Gününden Başlayarak)
print(an.strftime("%c"))    #Yerel Biçim Ayarlarına Göre Tarih Ve Saat
print(an.strftime("%x"))    #Yerel Biçim Ayarlarına Göre Tarih
print(an.strftime("%X"))    #Yerel Biçim Ayarlarına Göre Tarih Ve Saat
print(an.strftime("%%"))    #Karakter Girdisi
