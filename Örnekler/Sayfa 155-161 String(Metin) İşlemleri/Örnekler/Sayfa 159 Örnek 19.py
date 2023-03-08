cumle="  bilişim teknolojileri giriş  "

print(cumle.strip())       # Baştaki ve sondaki boşluklar silinir

print(cumle.strip(" bil")) # Boşluk ,b,i,l karakterleri silinir

print(cumle.strip("prg"))  #Parametre bulunmadığı için hiçbir karakter çıkarılmaz

cumle2="python çok kullanışlı"
print(cumle2.strip("pyt"))
