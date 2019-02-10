"""
Tema 45
Nalezeni k-teho nejvetsiho prvku v posloupnosti
"""

from random import randrange


try:
    n = int(input("pocet prvku: "))
    k = int(input("k-ty prvek: "))
    min = int(input("minimum: "))
    max = int(input("maximum: "))
except ValueError:
    print("Spatny vstup!")
    exit(1)


if n > 0 and k > 0 and k <= n:
    seznam = []
    for i in range(0,n):
        seznam.append(randrange(min,max))
    print(seznam)
    seznam.sort()
    print(seznam)
    print(seznam[-k])
else:
    print("Chybny vstup!")
