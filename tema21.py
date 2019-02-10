"""
Tema 21
Operace se zlomky: soucet, nasobeni, deleni, kraceni

ve tvaru:
a/b = p/q operator r/s
"""


def soucet(p, q, r, s):
    a = p*s + q*r
    b = q*s
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    return a, b


def nasobeni(p, q, r, s):
    a = p*r
    b = q*s
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    return a, b


def deleni(p, q, r, s):
    a = p*s
    b = q*r
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    return a, b


def kraceni(a, b):
    if b == 0:
        return a
    else:
        return kraceni(b, a % b)


p = 8.5
q = 2
r = 6
s = 5


if (type(p) == int or float) and (type(q) == int or float) and (type(r) == int or float) and (type(s) == int or float):
    if q == 0 or s == 0:
        print("Deleni nulou!")
    else:
        print(soucet(p, q, r, s))
        print(nasobeni(p, q, r, s))
        if r == 0:
            print("Deleni nulou!")
        else:
            print(deleni(p, q, r, s))
else:
    print("Spatny vstup!")
