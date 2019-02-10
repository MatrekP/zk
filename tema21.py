"""
Tema 21
Operace se zlomky: soucet, nasobeni, deleni, kraceni

ve tvaru:
a/b = p/q operator r/s
"""


def operace(p, q, r, s):
    if q == 0 or s == 0:
        print("Deleni nulou!")
    else:
        print(soucet(p, q, r, s))
        print(nasobeni(p, q, r, s))
        if r == 0:
            print("Deleni nulou!")
        else:
            print(deleni(p, q, r, s))


def soucet(p, q, r, s):
    a = p*s + q*r
    b = q*s
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    if b == 1:
        return a
    else:
        return a, b


def nasobeni(p, q, r, s):
    a = p*r
    b = q*s
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    if b == 1:
        return a
    else:
        return a, b


def deleni(p, q, r, s):
    a = p*s
    b = q*r
    delitel = kraceni(a, b)
    a = a / delitel
    b = b / delitel
    if b == 1:
        return a
    else:
        return a, b


def kraceni(a, b):
    # if b == 0:
    #     return a
    # else:
    #     return kraceni(b, a % b)
    return 1


# try:
#     p = float(input("p: "))
#     q = float(input("q: "))
#     r = float(input("r: "))
#     s = float(input("s: "))
# except ValueError:
#     print("Spatny vstup!")
#     exit(1)

p = 2
q = 3.2
r = 5
s = 2
operace(p, q, r, s)
