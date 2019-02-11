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

K nalezení k-tého největšího prvku v posloupnosti stačí takovou posloupnost získat, seřadit podle velikosti a nalézt k-tý největší prvek. Při psaní svého programu vycházím z předpokladu, že obor hodnot posloupnosti je množina přirozených čísel.

Program je interaktivní a po spuštění vyžaduje zadání od uživatele 4 parametrů v tomto pořadí: počet prvků v posloupnosti n, kolikátý k-tý největší prvek má být nalezen, minimální hodnoty prvku a maximální hodnoty prvku. Jestliže uživatel zadá jiná než celá čísla, program skončí s chybou 1.
Následně program zkoumá, zda-li je zadaný počet prvků v posloupnosti kladný, pořadí hledaného největšího prvku rovněž tak, a zda je toto pořadí rovno či menší než celkový počet prvků v posloupnosti.
Jestliže jsou tyto podmínky splněny, je pro vyřešení problému nejprve potřeba vytvořit posloupnost, a tak program přistupuje k vytvoření a naplnění seznamu dle zadaných parametrů uživatelem. K tomuto účelu jsem využil funkci randrange() z knihovny random. Dále seznam setřídí od nejmenšího po největší, vytiskne hodnotu k-tého největšího prvku v posloupnosti a skončí.

Můj algoritmus používá globální proměnné n, k, min, max datového typu integer a seznam typu seznam a lokální proměnnou i typu integer. Program nepoužívá žádné nově vytvořené funkce, protože se kromě jednoduchého for cyklu nikde nepoužívá opakování kódu. Z funkcí používá int() k převodu výstupu z funkce input() z datového typu str do int. Algoritmus využívá test try – except ValueError ke zkoušce správnosti vstupu. V kódu je obsažena podmínka if – else pro zkontrolování správnosti oboru hodnot vstupu a také for cyklus k naplnění seznamu pseudo-náhodnými celými čísly generované funkcí randrange() z naimportované knihovny random, přičemž toto přidávání prvků se děje pomocí funkce .append(). Při třídění prvků v seznamu používá program .sort(). K vypsání výsledků algoritmu je užita funkce print(). Protože je seznam seřazený funkcí .sort() od nejmenšího po největší, samotné hledání hodnoty k-tého největšího prvku posloupnosti aplikace nakonec jednoduše dokončí tiskem hodnoty prvku posloupnosti takového pořadí, jaká je opačná hodnota proměnné k. 

Uživatel postupně zadá 4 proměnné n, k, min a max v tomto pořadí. Uživatel používá pouze přirozená čísla a potvrzuje jednotlivá zadání stiskem klávesy enter.
Program vytiskne ve třech řádcích vygenerovaný seznam celých čísel, z něj setříděnou posloupnost a hodnotu k-tého největšího prvku.

Problematickým místem se stává, když uživatel zadá moc vysoký počet prvků posloupnosti, než je přiměřené, či zadá větší rozsah oboru hodnot prvků posloupnosti než vhodný, protože by mohlo hrozit „přetečení“ proměnných či snad jiné renoncy.
Z možných vylepšení bych viděl jistý prostor při zadávání vstupu například možností vytvoření vlastní posloupnosti uživatelem či načtení posloupnosti ze souboru. Stejně tak výstup může být řešen rozličnými jinými způsoby. Časová složitost algoritmu nebyla při psaní programu zkoumána, což právě v tomto může tkvět případné zefektivnění kódu.
