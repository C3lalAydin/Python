def onakadar_say():    #onakadar_say diye bir fonksiyon oluşturup içine 10 a kadar sayan kod yazıldı
    a=0
    while a<10:
        a+=1
        print(a)


onakadar_say()   #Fonksiyon Çağrıldı


#Aşağıda Aynı Örneğin For Dögüsü İle Gerçekleştirilmiş hali Gösterilmektedir.

print("-"*15)  #Üsteki Çıktı İle Karışmasın Diye 15 Tane "-" işareti Koyulmuştur.

def ondefa_yaz():              #ondefa_yaz diye bir fonksiyon oluşturup içine 10 kere "Merhaba Arkadaşlar !" diyen kod yazıldı
    for x in range(1,10):
        print("Merhaba Arkadaşlar !")

ondefa_yaz() #Fonksiyon Çağrıldı
