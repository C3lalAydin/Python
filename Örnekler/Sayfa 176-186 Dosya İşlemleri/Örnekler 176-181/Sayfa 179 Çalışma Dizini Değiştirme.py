import os
dizin=os.getcwd() #os.getcwd() Fonksiyonu Çalışma Dizininin Yoludur
print(dizin)


try:
    os.chdir("C:\\test")  #Programın Çalışma Dizini "C:\test" olarak Ayarlanmıştır
    yeni_dizin=os.getcwd()
    print(yeni_dizin)

except FileNotFoundError:
    print("Böyle Bir Yol Bulunamadı")
    os.mkdir("C:\\test")
    print("Oluşturluyor....")
    
