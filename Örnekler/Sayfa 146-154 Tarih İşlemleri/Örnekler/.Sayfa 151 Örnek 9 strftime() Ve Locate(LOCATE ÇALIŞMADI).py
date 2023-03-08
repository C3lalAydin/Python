import datetime
import locale

locale.setlocale(locale.LC_ALL, 'Turkish.Turkey.1254')

an=datetime.datetime.now()

print(an.strftime("%Y"))    #Yıl
print(an.strftime("%X"))    #Saat
print(an.strftime("%d"))    #Gün - Ayın Kaçıncı Günü
print(an.strftime("%A"))    #Gün - İsim olarak
print(an.strftime("%B"))    #Ay - İsim Olarak
