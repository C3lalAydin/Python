sayi=input("Rakamları Toplancak Sayı Giriniz: ")
liste=list(sayi)
toplam=0

for x in range(0,len(liste)):
    toplam+=int(liste[x])

print("{} Sayısının Rakamlarının Toplamı {}".format(sayi,toplam))
