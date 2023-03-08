def artik_yil(yil):
    artik=False
    if yil%4==0 and yil%100!=0:
        artik=True
    return artik

def yilin_gunu(gun,ay,yil):
    gunler=[31,28,31,30,31,30,31,31,30,31,30,31]
    if artik_yil(yil):
        gunler[1]=29
    sira=0
    for x in range(ay-1):
        sira+=gunler[x]
    sira+=gun
    return sira

print(yilin_gunu(1,2,2007))
