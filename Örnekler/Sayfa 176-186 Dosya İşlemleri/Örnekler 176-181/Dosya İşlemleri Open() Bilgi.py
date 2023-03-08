"""
Mevcut Dosyayı Açmak için open() Fonskiyonu kullanılır
open() fonksiyonu  dosya ismi ve mod(dosya açma biçimi) olarak iki parametre alır.
Dosyayı açmak için 4 farklı mod kullanılır

"r" - Okuma  : Okumak İçin Bir Dosya Açar Dosya Hedefte Yoksa Hata Verir(Varsayılan)
"a" - Ekleme : Var Olan Dosyayı Düzenleme Yapmak İçin Açar Dosya Yoksa Oluşturur
"w" - Yazma  : Yazma Modunda Bir Dosya Açar Dosya Hedefte Yoksa Oluşturur
"x" - Oluştur: Belirtilen Dosyayı Oluşturur Dosya Varsa Hata Verir

read()      = Fonskiyonu Açılmış dosyanın içeriğini tek bir metin olarak okur
readline()  = İlk Satırı okur bir daha yazılırsa 2. Birdaha yazılınca 3. ..... Satırı okur
readlines() = Bütün Dosyayı Listeye Ekleme Yardımcı olur

Açılan Her Dosya Belleğe Atılır Hafızada Yer Kaplar Bu Nedenle Verimli Bellek Yönetimi İçin
Dosyalar Çalışma Sonunda close() Fonksiyonu ile kapatılmalıdır

"""
