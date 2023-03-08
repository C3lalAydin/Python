kelime="Gaziantep"
print("G" in kelime)   #kelimenin içinde G harfini Aratıyoruz
print("k" in kelime)   #Kelimenin içinde K harfini Aratıyoruz

print("-"*15)  #Yukarıyı Ayırmak İçin

print("G" not in kelime)   #not fonksiyonu ile tersine çevriliyor
print("k" not in kelime)   #not fonksiyonu ile tersine çevriliyor

print("-"*15)  #Yukarıyı Ayırmak İçin


ara=input("Arancak Harfi Giriniz: ")
sira_bul=(kelime.find(ara))+1

if sira_bul<0:
    print("{} Harfi Kelimede Yok".format(ara))
else:
    print("{} Harfi Kelimede Var.Kelimede {}. Sırada Yer Alıyor".format(ara,sira_bul))
