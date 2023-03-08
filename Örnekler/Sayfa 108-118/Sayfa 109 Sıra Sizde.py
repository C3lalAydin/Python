ifade=input("Bir İfade Giriniz: ")
harf=input("Bir Harf Giriniz: ")

harf_sayisi=0

for x in ifade:
    if x==harf:
        harf_sayisi+=1
print('{} Kelimesinde {} Tane "{}" Harfi Var'.format(ifade,harf_sayisi,harf))
