def tumevarim(sayi):
    if sayi==1:
        return 1
    else:
        return sayi+tumevarim(sayi-1)

print(tumevarim(5))
