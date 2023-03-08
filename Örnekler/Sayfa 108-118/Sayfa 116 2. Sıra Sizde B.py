import random

sayi=random.randint(0,20)

while True:
    sec=int(input("0 ile 20 Arası Bir Sayı Seçtim Bulmaya Çalış: "))
    if sec==sayi:
        print("Tebrikler Doğru Bildiniz")
        break
    if sec<sayi:
        print("Birazdaha Yukarı Çıkın")
    if sec>sayi:
        print("Biraz Aşağıya İnin")
