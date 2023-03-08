import os
dizin=os.getcwd()  #Olduğumuz Dizini Gösterir
print(dizin)

print("-"*15)     #Yukarı yı aşağıdan ayırmak için

"""
Mevcut çalışma dizinini değiştiremk için chdir() fonksiyonu kullanılır
"""

#import os
os.chdir("c:\\test")
yeni_dizin=os.getcwd()
print(yeni_dizin)

"""
C sürücüsünde "test" klasörü olmadığı için hata verir
"""
