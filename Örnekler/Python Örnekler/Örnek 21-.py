sayilar=0
sayi=int(input("Sayı Giriniz: "))
for x in range(2,sayi):
      if sayi%x==0:
            sayilar+=1
            break
if not sayilar==0:
      print("{} Sayısı Asal Değil".format(sayi))
else:
      print("{} Sayısı Asaldır".format(sayi))
