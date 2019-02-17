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
    max = int(input("maximum: ")) + 1
except ValueError:
    print("Spatny vstup!")
    exit(1)

# zkontrolovani spravnosti oboru hodnot vstupu s vytvorenim posloupnosti a nalezením k-teho nejvetsiho prvku
if n > 0 and k > 0 and k <= n and min < max:
    seznam = []
    for i in range(0,n):
        seznam.append(randrange(min, max))
    print("seznam: {}".format(seznam))
    seznam.sort()
    print("posloupnost: {}".format(seznam))
    print("{}. nejvetsi prvek posloupnosti je {}.".format(k, seznam[-k]))
else:
    print("Spatny vstup!")
    exit(1)
print("Pekny den.")
