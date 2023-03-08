def carpan(n):
    return lambda a:a*n

ikikat=carpan(2)
uckat=carpan(3)
dortkat=carpan(4)

print(ikikat(10))
print(uckat(10))
print(dortkat(10))
