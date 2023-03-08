import os
os.chdir("C:\\test")

dosya=open("milli.txt")  #Dosya Açılır
for satir in dosya:
    print(satir.upper(),end=" ")
dosya.close()  #dosya kapatılır
