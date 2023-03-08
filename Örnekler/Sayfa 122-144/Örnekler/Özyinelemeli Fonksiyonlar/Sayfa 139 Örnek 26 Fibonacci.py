def fibonacciler(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacciler(n-1)+fibonacciler(n-2)         #Örnek n 5 e eşitse 5-1=4   5-2=3  4+3=8 Olur Sonra n 8 Eşitse 8-1=7  8-2=6  7+6=13....

for i in range(1,21):
    print(fibonacciler(i),end=" ")

print()
