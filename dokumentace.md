Téma 21 - Operace se zlomky: součet, násobení, dělení, krácení
rozbor problému
existující algoritmy
popis zvoleného algoritmu
struktura programu (datové struktury, metody, …)
popis vstupních/výstupních dat
problematická místa
možná vylepšení
Předmětem zadání je napsat zdrojový kód aplikace pro základní operace se zlomky, tedy součet, násobení, dělení a krácení. Rozhodl jsem se ukázat jednoduché řešení v jazyce Python 3 pro dva zlomky ve tvaru p/q (operátor) r/s. Výsledek je po zkrácení vypsán ve tvaru a/b.

Téma 45 – Nalezení k-tého největšího prvku v posloupnosti
rozbor problému
existující algoritmy
popis zvoleného algoritmu
struktura programu (datové struktury, metody, …)
popis vstupních/výstupních dat
problematická místa
možná vylepšení
Program je interaktivní a po spuštění vyžaduje zadání od uživatele 4 parametrů v tomto pořadí: počet prvků v posloupnosti n, kolikátý k-tý největší prvek má být nalezen, minimální hodnoty prvku a maximální hodnoty prvku. Jestliže uživatel zadá jiná než celá čísla, program skončí s chybou 1. 
Následně program zkoumá, zda-li je zadaný počet prvků v posloupnosti kladný, pořadí hledaného největšího prvku rovněž tak, a zda je toto pořadí rovno či menší než celkový počet prvků v posloupnosti.
Jestliže jsou tyto podmínky splněny, je pro vyřešení problému nejprve potřeba vytvořit posloupnost, a tak program přistupuje k vytvoření a naplnění seznamu dle zadaných parametrů uživatelem. K tomuto účelu jsem využil funkci randrange() z knihovny random. Dále seznam setřídí od nejmenšího po největší, vytiskne hodnotu k-tého největšího prvku v posloupnosti, popřeje odpočinek v pokoji a skončí.
Program splnil zadání, protože, pokud k tomu dostane korektní vstup, nalezne k-tý největší prvek v posloupnosti. V opačném případě upozorní na chybu a skončí.
