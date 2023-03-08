dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","w")       #Yeni Dosya Oluşturuyor
dosya.write("Nasilsin")     #Dosyanın İçine Nasılsın yazıyor


dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","a")       #Dosyayı Düzenliyor
dosya.write(" iyi misin")   #Nasılsının Yanına iyi misin yazıyor

'''
w = Yeni Dosya Açma (O Adda bir Dosya Varsa Onu Siler Yenisini Açar)  w=Write
a = Dosyanın İçine Ekleme Yapar (O Adda Bir Dosya Yoksa Yeni Dosya Olulturur) a=Append
'''

dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","r")      #Dosyayı Okuyor

"""
r = Dosyayı Okumaya Yarar
"""

"""
read()       Bütün Dosyayı okur
readline()   İlk Satırı okur bir daha yazılırsa 2. Birdaha yazılınca 3. ..... Satırı okur
readlines()  Bütün Dosyayı Listeye Ekleme Yardımcı olur
"""
dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","r")
print(dosya.read())

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","r")
print(dosya.readline())

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

dosya=open("C:/Users/Celal Aydin/Desktop/yazilim.txt","r")
liste=dosya.readlines()
print(liste)
