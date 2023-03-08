import random     #Kütüphaneden Random Fonksiyonu Yükelnir
while True:
    n=random.randint(1,20)     #1 ile 20 Arasında Random Sayı Seçem Komut
    print("Rastgele Seçilen Sayı {}".format(n))
    if n%2==0:    #Random Gelen Sayı Çift Sayı ise Döngü Sonlandırılır
        print("{} Sayısı Çift Sayı Olduğu İçin Döngü Bitti")
        break
