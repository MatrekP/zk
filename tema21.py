"""
Tema 21
Operace se zlomky: soucet, nasobeni, deleni, kraceni

ve tvaru:
a/b = p/q operator r/s
"""


def operace(p, q, r, s):
    """

    :param p:
    :param q:
    :param r:
    :param s:
    :return:
    """
    if q == 0 or s == 0:
        print("Deleni nulou!")
    else:
        print("soucet: ", end="")
        print(soucet(p, q, r, s))
        print("nasobeni: ", end="")
        print(nasobeni(p, q, r, s))
        if r == 0:
            print("Deleni nulou!")
        else:
            print("deleni: ", end="")
            print(deleni(p, q, r, s))


def soucet(p, q, r, s):
    """

    :param p:
    :param q:
    :param r:
    :param s:
    :return:
    """
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
    """

    :param p:
    :param q:
    :param r:
    :param s:
    :return:
    """
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
    """

    :param p:
    :param q:
    :param r:
    :param s:
    :return:
    """
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
    """

    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return kraceni(b, a % b)

# zadani vstupu se zkouskou spravnosti
try:
    p = int(input("p: "))
    q = int(input("q: "))
    r = int(input("r: "))
    s = int(input("s: "))
except ValueError:
    print("Spatny vstup!")
    exit(1)

# vykonani operaci
operace(p, q, r, s)
