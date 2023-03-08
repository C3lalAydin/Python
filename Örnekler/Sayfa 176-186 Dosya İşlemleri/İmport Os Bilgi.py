import os
import datetime
cekirdek=os.name      #Eğer Kodlarımızı Windowsda çalıştırdıysak nt Macos ve Gnu/linux da posix cevabınımı alırız
print("Hangi İşletim sistemi: ",cekirdek)

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

dizin_araci=os.sep    #kodlarımızın çalıştığı işletim sisteminin dizin ayracının ne olduğunu bize gösterir
print("Dizin Aracı: ",dizin_araci)

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

mevcut_dizin=os.getcwd()     #Şuanda içinde bulunduğumuz dizinin adını verir
print("Şuanda İçinde Olduğumuz Dizin: ",mevcut_dizin)

dizin_degistirme=os.chdir("C:\\Users\\Celal Aydin\\Desktop")    #chider() bize bir dizinden başka bir dizine geçme imkanı verir
print(dizin_degistirme)

dizin_listeleme=os.listdir(mevcut_dizin)   #Yazdığımız Dizinin İçindekilerini Listeler
print("Mevcut Dizinin İçindekiler: ",dizin_listeleme)

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

deneme_txt="C:/Users/Celal Aydin/Desktop/Programlama/Sayfa 176-186 Dosya İşlemleri/deneme.txt"
print("deneme.txt Çalıştırılıyor...")
#os.startfile(deneme_txt)   #Bilgisayarda olan dosyayı/Programı Açar

print("Mevcut Dizin Açılıyor...")
#os.startfile(mevcut_dizin) #Dosya değilde dizin adı verirsek explorer da o dizini açar

print("Google Açılıyor...")
#os.startfile("www.google.com")  #Startfile ile İnternet siteside Açabilirsiniz

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

#try:
    #os.mkdir("C:/Users/Celal Aydin/Desktop/yeni_dizin")   #Mkdir Yeni Dizin açmanızı Sağlar
#except FileExistsError:                    #Dizin Zten varsa Vercek Yanıt
    #print("Böyle Bir Dizin Zaten Var")

"""
Bu komutun çalışabilmesi için, bilgisayarımızda halihazırda C:/Users/Celal Aydin/Desktop yolunun varolması gerekir.
Eğer bu yolu oluşturan dizinlerden herhangi biri mevcut değilse
 mkdir() fonksiyonu yenidizin adlı dizini oluşturamaz.

 os.makedirs() ise os.mkdir() fonksiyonunun aksine
 varolmayan üst ve alt dizinleri de oluşturma yeteneğine sahiptir
"""
#Örnek

#try:
    #os.makedirs("C:/Users/Celal Aydin/Desktop/Yeni Bir Klasör/Yeni Dizin/Deneme")
#except FileExistsError:                    #Dizin Zten varsa Vercek Yanıt
    #print("Böyle Bir Dizin Zaten Var")


#try:
    #os.rename("C:/Users/Celal Aydin/Desktop/Yeni Bir Klasör/Yeni Dizin/Deneme","Test_Deneme")
#except FileExistsError:                    #Dizin Zten varsa Vercek Yanıt
    #print("Böyle Bir Dizin Zaten Var")
"""
os.rename('dizinin_şimdiki_adı', 'dizinin_yeni_adı') Şeklinde Çalışır

Eğer zaten Test_Deneme adlı bir dizin varsa (ve içi boşsa), yukarıdaki komut GNU/Linux’ta Test_Deneme
adlı dizinin üzerine yazacak, Windows’ta ise hata verecektir.
"""

#os.replace("Test_Deneme","Deneme123")

"""
Bu komut, tıpkı rename() fonksiyonunda olduğu gibi, deneme adlı dizinin adını test olarak değiştirecektir.

Eğer test adlı bir dizin zaten varsa, replace() fonksiyonu, hem Windows’ta hem de GNU/Linux’ta
varolan bu test dizininin üzerine yazmaya çalışır
GNU/Linux’ta çoğu durumda bunu başarır, ancak Windows’ta yine de çeşitli izin hataları ile karşılaşabilirsiniz.
"""

#os.remove("Yeni Bir Klasör")   #os modülünün remove() adlı fonksiyonu, bilgisayarımızdaki dosyaları silmemizi sağlar

#os.rmdir('dizin_adı')  #os modülünün rmdir() fonksiyonu, içi boş bir dizini silmek için kullanılır
"""
Eğer silmeye çalıştığınız dizin içinde herhangi bir başka dizin veya dosya varsa bu fonksiyon hata verecektir.

Çünkü bu dizinlerinin hiçbirinin içi boş değil
her birinin içinde birer dizin var. Ama şu komut
başarılı olacaktır:

os.rmdir(r'anadizin/dizin1/dizin2/dizin3/dizin4')
"""

dosya=os.stat("C:/Users/Celal Aydin/Desktop/Programlama/Sayfa 176-186 Dosya İşlemleri/deneme.txt")   #Dosya Hakkında Bilgi Verir
print(dosya)
"""
st_atime:  dosyaya en son erişilme tarihi
st_ctime:  dosyanın oluşturulma tarihi (Windows’ta)
st_mtime:  dosyanın son değiştirilme tarihi
st_size:   dosyanın boyutu
"""

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

print("Dosyaya En Son Erişilen Tarih: ",dosya.st_atime)
print("Dosyayı Oluşturma Tarihi: ",dosya.st_ctime)
print("Dosyanın En Son Değiştirilme Tarihi: ",dosya.st_mtime)
print("Dosyanın Boyutu: ",dosya.st_size," Bayt")
"""
Bu arada, yukarıdaki komutların çıktısı size anlamsız gelmiş olabilir.
datetime modülündeki fromtimestamp() normal tarihe dönüştürebilriz:

    tarih_cevirme=datetime.datetime.fromtimestamp(dosya.st_ctime)
    print("Dosyayı Oluşturma Tarihi: ",tarih_cevirme)
"""

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

#os.system('notepad.exe')  #os.system() Sistem Komutlarını Ve Programlarını Çalıştırmayı Sağlar
