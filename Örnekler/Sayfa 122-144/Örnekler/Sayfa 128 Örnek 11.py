def selamla(ad):                         #Parametre Atandı
    print("Merhaba {}".format(ad))


"""
Fonksiyon yazılırken alacağı Parametre boş geçilmesi durumunda hata vercektir.
Hata Verilmemesi İçin Varsayılan Bir Değer Girmeliyiz
"""

selamla("Celal")
selamla("Ahmet")
selamla("Arda")
selamla("Ali")

selamla() #Varsayılan bir değer olmadığı için hata verir
