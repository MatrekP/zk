Téma 45 – Nalezení k-tého největšího prvku v posloupnosti
K nalezení k-tého největšího prvku v posloupnosti stačí takovou posloupnost získat, seřadit ji podle velikosti a vytisknout hodnotu prvku na správné pozici. Při psaní svého programu vycházím z předpokladu, že obor hodnot posloupnosti je množina přirozených čísel.

Program je interaktivní a po spuštění vyžaduje od uživatele zadání 4 parametrů v tomto pořadí: počet prvků v posloupnosti n, kolikátý k-tý největší prvek má být nalezen, minimální hodnoty prvku min a maximální hodnoty prvku max. Jestliže uživatel zadá jiná než celá čísla, program skončí s chybou 1.
V opačné případě program zkoumá, zda-li je zadaný počet prvků v posloupnosti kladný, pořadí hledaného největšího prvku rovněž tak, a zda je toto pořadí rovno či menší než celkový počet prvků v posloupnosti, a také jestli je minimální hodnota prvku menší než maximální.
Jestliže jsou tyto podmínky splněny, je pro vyřešení problému nejprve potřeba vytvořit posloupnost, a tak program přistupuje k vytvoření a naplnění seznamu dle zadaných parametrů uživatelem. K tomuto účelu jsem využil funkci randrange() z knihovny random. Dále program seznam setřídí od nejmenšího po největší, vytiskne hodnotu k-tého největšího prvku v posloupnosti, popřeje pěkný den a skončí.

Můj algoritmus používá globální proměnné n, k, min, max datového typu integer a seznam typu seznam a lokální proměnnou i typu integer. Program nepoužívá žádné nově vytvořené funkce, protože se kromě jednoduchého for cyklu nikde nepoužívá opakování kódu a z toho titulu, že má méně než 30 platných řádek, a je tudíž poněkud nedlouhý. Z funkcí používá int() k přetypování výstupu z funkce input() z datového typu string do integer. Algoritmus využívá test try – except ValueError ke zkoušce správnosti vstupu. V kódu je obsažena podmínka if – else pro zkontrolování správnosti oboru hodnot vstupu a také for cyklus k naplnění seznamu pseudo-náhodnými celými čísly generované funkcí randrange() z naimportované knihovny random, přičemž toto přidávání prvků se děje pomocí funkce .append(). Při třídění prvků v seznamu používá program .sort(). K vypsání výsledků algoritmu je užita funkce print(). Protože je seznam seřazený funkcí .sort() od nejmenšího po největší, samotné hledání hodnoty k-tého největšího prvku posloupnosti aplikace nakonec jednoduše dokončí tiskem hodnoty prvku posloupnosti takového pořadí, jaká je opačná hodnota proměnné k.

Vstup: Uživatel postupně zadá 4 proměnné n, k, min a max v tomto pořadí. Uživatel používá u proměnných n, k pouze přirozená čísla, u min, a max celá čísla a potvrzuje jednotlivá zadání stiskem klávesy enter.
Výstup: Program vytiskne ve třech řádcích vygenerovaný seznam celých čísel, z něj setříděnou posloupnost a hodnotu k-tého největšího prvku. V případech chybného zadání vstupu program tiskne chybovou hlášku.

Problematickým místem se stává rozsah hodnot, kterých mohou prvky posloupnosti nabývat. Musí být připočtena 1 k zadanému maximu, protože jsem zjistil, že funkce randrange() bere interval minima a maxima zleva uzavřený, ale zprava otevřený.

Z možných vylepšení bych viděl jistý prostor při zadávání vstupu například možností vytvoření vlastní posloupnosti uživatelem či načtení posloupnosti ze souboru. Stejně tak výstup může být řešen rozličnými způsoby. Časová složitost algoritmu ani jeho náročnost na systémové prostředky nebyly při psaní programu zkoumány, což právě v tomto může tkvět případné zefektivnění kódu.



Zdrojový kód aplikace:
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
    print('seznam: {}'.format(seznam))
    seznam.sort()
    print('posloupnost: {}'.format(seznam))
    print('{}. nejvetsi prvek posloupnosti je {}.'.format(k, seznam[-k]))
else:
    print("Spatny vstup!")
    exit(1)
print("Pekny den.")



 
Vstupní/výstupní data
 
Příklad 1 běhu programu:
pocet prvku: 5
k-ty nejvetsi prvek: 2
minimum: -10
maximum: 10
seznam: [4, -2, 1, -9, 9]
posloupnost: [-9, -2, 1, 4, 9]
2. nejvetsi prvek posloupnosti je 4.
Pekny den. 

Process finished with exit code 0

Příklad 2 běhu programu:
pocet prvku: 2
k-ty nejvetsi prvek: 3
minimum: 1
maximum: 100
Spatny vstup!

Process finished with exit code 1

Příklad 3 běhu programu:
pocet prvku: 6.66
Spatny vstup!

Process finished with exit code 1

Příklad 4 běhu programu:
pocet prvku: p
Spatny vstup!

Process finished with exit code 1

Příklad 5 běhu programu:
pocet prvku: -13
k-ty nejvetsi prvek: 20
minimum: -1
maximum: -2
Spatny vstup!

Process finished with exit code 1

 

