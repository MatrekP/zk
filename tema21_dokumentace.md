Téma 21 - Operace se zlomky: součet, násobení, dělení, krácení
Předmětem zadání je napsat v jazyce Python 3 zdrojový kód aplikace pro základní operace se zlomky, tedy součet, násobení, dělení a krácení. Rozhodl jsem se ukázat jednoduché řešení pro dva zlomky ve tvaru p/q (operátor) r/s. Výsledek je po zkrácení vypsán ve tvaru a/b. V případě, že je b = 1, je vypsáno pouze a.

Stanovit hodnotu největšího společného dělitele proměnných a a b, tolik důležitou pro krácení zlomků, lze různými způsoby. Lze projít všechna čísla od 1 do min(a, b), pro každé vyzkoušet, zda dělí a i b a to největší bude kýžený dělitel. Dá se také využít rozkladu a a b na součin prvočísel, vybrat společné a vzájemně je vynásobit. A konečně je možné využít takzvaný Eukleidův algoritmus, který jsem použil, protože elegantně v několika málo výpočtech dokáže najít největší společný dělitel. U první zavrhnuté varianty je třeba hledat všechny dělitele, ukládat je do seznamu a vybrat ten největší. U druhé varianty algoritmu je navíc nutné vypočítávat prvočísla a postupně je zkoušet, zda nejsou děliteli a, b a vybírat společné. Eukleidův algoritmus pracuje tak, že do b uloží zbytek po dělení původního a a b. A to vykonává stále dokola, dokud není b nulové. Potom je největší společný dělitel uložen v a. Z těchto důvodů jsem do programu implementoval algoritmus starověkého filosofa Eukleida.

Program po spuštění vyzve uživatele, aby zadal 4 proměnné p, q, r, s v tomto pořadí. Uživatel zadává pouze celá čísla a potvrzuje jednotlivé vstupní hodnoty stiskem klávesy enter. Pokud uživatel zadá nekorektní vstup, program vytiskne výstražnou hlášku a skončí s chybou. 
V opačném případě program předá hodnoty proměnných do funkce operace(p, q, r, s), která vyšetřuje, zda p a s, jmenovatelé, se nerovnají nule, a v případě dělení zda se r nerovná nule. Jestliže jsou tyto podmínky splněny, dojde k volání funkcí soucet(p, q, r, s), nasobeni(p, q, r, s) a deleni(p, q, r, s), které vracejí výsledky, tj. čitatel a jmenovatel a/b, případně jen čitatel a, jestliže je b rovno 1.
Tyto tři funkce vypočítávají výsledky dle níže uvedených vzorců pro součet (1), násobení (2) a dělení (3). 
	a/b=p/q+r/s=(ps+qr)/qs	(1)
	a/b=p/q∙r/s=pr/qs	(2)
	a/b=p/q:r/s=ps/qr	(3)
 
V každé z těchto funkcí je začleněno volání rekurzivní funkce kraceni(a, b), která vrací největší společný dělitel, kterým je každý výsledek operace se zlomky vydělen. Tak je docíleno zkrácení zlomku do základního tvaru. Výsledky, resp. chybové hlášky jsou na závěr vypsány a program skončí.

Algoritmus využívá globální proměnné p, q, r, s typu integer a lokální proměnné a, b ve funkcích soucet(), nasobeni(), deleni() a kraceni(). Dále algoritmus používá funkce int() pro přetypování výstupu z funkce input() ze string na integer. Pro výpis výsledků či chybových hlášek používá print(). Ve funkci operace(p, q, r, s) jsou obsaženy podmínky if – else, protože je třeba zabránit dělení nulou. Funkce soucet(p, q, r, s), nasobeni(p, q, r, s) a deleni(p, q, r, s) počítají výsledky operací podle výše uvedených vzorců a vždy je učiněn pokus o zkrácení zlomku na základní tvar. Toto krácení zlomků probíhá způsobem, že se vypočte největší společný dělitel čitatele a jmenovatele a tímto dělitelem se oba členy zlomku podělí. Vypočítání největšího dělitele se provádí rekurzivně pomocí Eukleidova algoritmu.

Vstup je řešen vyzváním uživatele k zadání celých čísel p, q, r, s v tomto pořadí, přičemž za korektní vstup se považují celá čísla. Výstup programu je uživateli vytisknut.

Problémem programu je jeho nefunkčnost pro větší než malé hodnoty proměnných p, q, r, s.
Celý algoritmus je možné vylepšovat. Jedno takové zdokonalení se nabízí v umožnění pracovat i s jiným oborem hodnot, než jsou celá čísla.
Zdrojový kód aplikace:
"""
Tema 21
Operace se zlomky: soucet, nasobeni, deleni, kraceni

ve tvaru:
a/b = p/q [operator] r/s
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


Vstupní/výstupní data
 
Příklad 1 běhu programu:
p: 2
q: 3
r: 5
s: 2
soucet: (19.0, 6.0)
nasobeni: (5.0, 3.0)
deleni: (4.0, 15.0)

Process finished with exit code 0

Příklad 2 běhu programu:
p: -3
q: 8
r: 45
s: 6
soucet: (57.0, 8.0)
nasobeni: (-45.0, 16.0)
deleni: (-1.0, 20.0)

Process finished with exit code 0

Příklad 3 běhu programu:
p: 4
q: -9
r: 17
s: -71
soucet: (-437.0, 639.0)
nasobeni: (68.0, 639.0)
deleni: (284.0, 153.0)

Process finished with exit code 0
 
Příklad 4 běhu programu:
p: -6
q: 25
r: 0
s: 1
soucet: (-6.0, 25.0)
nasobeni: 0.0
Deleni nulou!

Process finished with exit code 0

Příklad 5 běhu programu:
p: 4
q: 1.2
Spatny vstup!

Process finished with exit code 1





Příklad 6 běhu programu:
p: 4
q: p
Spatny vstup!

Process finished with exit code 1
