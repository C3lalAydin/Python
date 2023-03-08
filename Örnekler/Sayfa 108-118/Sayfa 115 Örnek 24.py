sayilar=[10,11,12,13,14,15,16]
arancak_sayi=int(input("Arancak Sayıyı Giriniz: "))

for aranan in sayilar:                        #Bu örnekte Kullanıcının Seçtiği Sayı Bulunduğunda Döngüden Çıkılmıştır
    print(aranan)
    if aranan==arancak_sayi:
        print("{} Sayısı Bulundu".format(arancak_sayi))
        break
