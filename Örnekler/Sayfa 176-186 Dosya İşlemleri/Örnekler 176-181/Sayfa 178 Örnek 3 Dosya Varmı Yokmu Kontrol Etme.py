import os
yol=os.path.join("C:\\","test")
if os.path.exists(yol):  #esists() Yolun Var olup  Olmadığını Kontrol Eder
    print(yol+" : var")
    if os.path.isdir(yol):   #isdir() Dizinin Olup Olmadığını Kontrol Eder
        print(yol+" : Bu Bir Dizin")
else:
    print("Yol Bulunamadı")
