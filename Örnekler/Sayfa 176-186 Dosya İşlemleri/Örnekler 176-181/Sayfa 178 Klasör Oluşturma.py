import os
yol=os.path.join("C:\\","test2")
if os.path.exists(yol):  #esists() Yolun Var olup  Olmadığını Kontrol Eder
    print(yol+" : var")
    if os.path.isdir(yol):   #isdir() Dizinin Olup Olmadığını Kontrol Eder
        print(yol+" : Bu Bir Dizin")
else:
    print("Yol Bulunamadı")
    os.mkdir(yol)   #mkdir() Fonskiyonu ile belirtilen yola("C:\test2") klasör oluşturuluyor
    print("Oluşturluyor...")
