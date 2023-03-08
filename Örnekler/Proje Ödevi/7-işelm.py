print("İki Sayı Giriniz Sonrada İşlem İşaretini Giriniz")
sayi1=int(input("1. Sayıyı Giriniz: "))
sayi2=int(input("2. Sayıyı Giriniz: "))
islem=(input("\nİşlem İşaretini Seçiniz\n\nToplama(+)\nÇıkarma(-)\nÇarpma(*)\nBölme(/)\nMod Alma(%)\nKuvvet Alma(**)\nTam Bölme(//)\n\nİşlemin İşaretini Yazın: "))

if islem=="+":
    print("Topladım Sonuç ",sayi1+sayi2)

if islem=="-":
    print("Çıkardım Sonuç ",sayi1-sayi2)

if islem=="*":
    print("Çarptım Sonuç ",sayi1*sayi2)

if islem=="/":
    print("Böldüm Sonuç ",sayi1/sayi2)

if islem=="%":
    print("Modunu Aldım Sonuç ",sayi1%sayi2)

if islem=="**":
    print("Kuvvetini Aldım Sonuç ",sayi1**sayi2)

if islem=="//":
    print("Tam Böldüm Sonuç ",sayi1//sayi2)
