veri="Bilişim Teknolojileri"
metin="ilkbahar,yaz,sonbahar,kış"

veri_bolum=veri.split(" ")   #Veri değişkenini boşluktan itibaren bölüyoruz
metin_bolum=metin.split(",") #Metin Değişkenini virgüllerden itibaren bölüyoruz

metin_bolum_ikieleman=metin.split(",",1) #1 Parametresi Vererek metni sadece iki parçaya bölüyoruz

print(veri_bolum)
print(metin_bolum)
print(metin_bolum_ikieleman)
