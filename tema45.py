"""
Tema 45
Nalezeni k-teho nejvetsiho prvku v posloupnosti
"""

from random import randrange


# zadani vstupu se zkouskou spravnosti vstupu
try:
    n = int(input("pocet prvku: "))
    k = int(input("k-ty nejvetsi prvek: "))
    min = int(input("minimum: "))
    max = int(input("maximum: "))
except ValueError:
    print("Spatny vstup!")
    exit(1)


# zkontrolovani spravnosti oboru hodnot vstupu s vytvorenim posloupnosti a nalezením k-teho nejvetsiho prvku
if n > 0 and k > 0 and k <= n and min > 0 and max > 0:
    seznam = []
    for i in range(0,n):
        seznam.append(randrange(min, max))
    print(seznam)
    seznam.sort()
    print(seznam)
    print(seznam[-k])
    print("Odpocivej v pokoji.")
else:
    print("Chybny vstup!")
