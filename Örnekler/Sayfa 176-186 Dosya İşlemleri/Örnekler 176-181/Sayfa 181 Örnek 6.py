import os
os.chdir("C:\\test")
dosya=open("milli.txt")

print(dosya.readline()) #Mvcut satırı okur her çağrıldığında bir sonraki satırı getirir
print(dosya.readline())
