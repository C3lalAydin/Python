import os
yol="C:\\deneme"
os.mkdir(yol)   #deneme Adlı Dizin Oluşruluyor

if os.path.exists(yol):     #Eğer C:\deneme yolu varsa Böyle Bir Dizin Var De
    print("Böyle Bir Dizin Var")

else:
    print("Dizin Bulunamadı Oluşturluyor...")
    os.mkdir(yol)  #deneme Adlı Dizin Oluşturuyor

print("Dizin Adı Değiştirliyor...")
os.chdir("C:\\")        #Çalışma Dizini C:\ Yapılıyor
os.rename("deneme","test")    #Deneme Adlı Klasörün Adı Test Olarak Değiştirliyor
print("Dizin Siliniyor.....")
os.rmdir("test")          #Test Adlı Klasör Siliniyor
print("Dizin Silindi")
