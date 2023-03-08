sayi=int(input("Bir Sayı Giriniz: "))
for i in range(1,10):                               #10 dan Yüksek Bir Sayı Girilirse 9 a Kadar Döngü Devam Eder Ve 9 a Kadar Ekrana Yazar, 9 da Döngü Bittiği İçin 9 dan Sonrasını Yazmaz
    if i==sayi:
        break
    print(i)
print("Döngü Sona Erdi")
