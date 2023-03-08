import os
os.chdir("C:\\test")

dosya=open("hitabe.txt","w")   #Dosyayı Yazma Modunda Açar Bu Adda Dosya Yoksa, Bu adda Dosya Açar
dosya.write("Ey Türk Gençligi!\n")
dosya.write("Birinci Vazifen,\n")
dosya.write("Türk istiklalini,Türk Cumhuriyeti'ni,\n")
dosya.write("Ilelebet muhafaza ve müdafaa etmektir.")
dosya.close() #Dosyayı Kapatır
