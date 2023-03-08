import os
yol=os.path.join("test","python")
"""
join() Fonksiyonu windows için ters bölü(\),
Unix için bölü(/) işaretini bileşenlerin arasına ekleyerek birleştirir
Tek bir fonskiyon ile hem windows hemde unix işletim sisteminde doğru çalışacak "path" bilgisi oluşturulur
"""
print(yol)  #test\python (Windows ta)

pc=os.path.split(yol)
"""
split() Fonksiyonu verilen yol bilgisini parçalara ayırarak liste haline getirir
"""
print(pc) #('test','python')
