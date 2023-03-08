import random
random_sayi=random.randint(1,50)


while True:
    sayi=int(input("1 İle 50 Arasında Bir Sayı Seçtim Bul: "))
    if random_sayi==sayi:
        print("Tebrikler Bildin")
        break
    if sayi>random_sayi:
        print("Yüksek Söyledin Biraz İn")
    if sayi<random_sayi:
        print("Az Söyledin Biraz Çık")
