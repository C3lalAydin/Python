kelime="Bilişim Teknolojileri"

print(kelime.find("m")) #Kelime Metninin içinde "m" harfinin indexini arıyoz

print(kelime.find("i",4))  #4. indexten başlayarak metnin içinde "i" yi arıcak

print(kelime.find("i",1,7))  #1. indexten başlayarak 7. indexe kadar "i" yi arıcak

print(kelime.find("z"))   #Eğer Aradğımız veri metinde yoksa -1 olarak dondürcek


ara=input("İndexi Arancak Harfi Giriniz: ")
bul=kelime.find(ara)

print("{} Harfinin İndexi {}".format(ara,bul))
