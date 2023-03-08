sayi_sor=int(input("Sayı Giriniz: "))
print(" ")

sayi=sayi_sor+1
cift=0
tek=0

for x in range(1,sayi):
    if x%2==0:
        cift+=x
    if not x%2==0:
        tek+=x

print("1 İle {} Arasındaki".format(sayi_sor))
print("Çift Sayıların Toplamı {}".format(cift))
print("Tek Sayıların Toplamı {}".format(tek))
