# Herní automat 🎰

Tento projekt je kod na herni automaty naprogramovan v pythonu. Nechal jsem se inspirovat mým předešlým projektem kde jsem ztvarnil hru blackjack. Váš počateční balance je 100Kč. Hra obsahuje pár možností na výhry.

## Vysvětlení kódu

### Import knihovny
```python
import random
```

### Inicializace hry
```python
symboly = ["🍺","🍷","🍸","🍹","🍑","🍆"]
kredit = 100
pocet_3_ruzne_za_sebou = 0
```


`symboly`: Seznam symbolů, které se mohou objevit při zatočení.

`kredit`: Počáteční kredit hráče.

`pocet_3_ruzne_za_sebou`: Počítadlo pro případ 3 různých symbolů za sebou – slouží k útěchové výhře.

### Uvítání a úvodní informace
```python
print("🎰 Vítej ve výherním automatu!")
print("Za každé zatočení zaplatíš 10 Kč. Pokud padnou 3 stejné symboly, vyhráváš 50 Kč.")
```

Hra pokračuje, dokud má hráč alespoň 10 Kč.
Každé zatočení stojí 10 Kč.

### Vygenerování tahu
```python
tah = [random.choice(symboly) for _ in range(3)]
print(" | ".join(tah))
```

Vygenerují se 3 náhodné symboly a zobrazí se na řádku.

### Výherní podmínky
```python
 tah[0] == tah[1] == tah[2]:
    print("🎉 Jackpot! 3 stejné symboly! Vyhráváš 50 Kč!")
    kredit += 50
```

Hráč vyhrává 50 Kč za 3 stejné symboly.

```python
elif tah[0] == tah[1] or tah[1] == tah[2] or tah[0]==tah[2]:
    print(" Dvě stejné vedle sebe! Vyhráváš 15 Kč!")
    kredit += 15
```

Pokud padnou 3 různé symboly, počítadlo se zvýší o 1.

```python
if pocet_3_ruzne_za_sebou == 3:
    print("🎁 Útěcha! 3 různé padly 3x za sebou – dostáváš 5 Kč!")
    kredit += 5
    pocet_3_ruzne_za_sebou = 0
```

Pokud se 3 různé symboly objeví 3x za sebou, hráč získá útěchovou výhru 5 Kč.

```python
else:
    print("❌ Nic jsi nevyhrál.")
```

Pokud žádná výherní podmínka není splněna, hráč nic nevyhraje.

### Kontrola kreditu a možnost ukončení
```python
if kredit < 10:
    print(" Nemáš dost peněz na další hru. Konec.")
    break
```

Hráč má možnost hru dobrovolně ukončit.

Jak spustit kód

Ujistěte se, že máte nainstalovaný Python 3.

Uložte kód do souboru, např. automat.py.

Spusťte kód pomocí příkazu:

```
python automaty.py
```
## Poznámky
Pořád se to učím sám a řekl bych že delám pokroky i když je v podstatě jen cyklus furt dokola.

Chtěl bych poděkovat Betanu za inspiraci.

## Licence
Tento projekt je licencován pod licencí MIT.

## Nástroje: 

JetBrains s.r.o. (2000–2025). PyCharm. Dostupné z: https://www.jetbrains.com/pycharm/download/?section=windows [cit. 2025-5-8].

OpenAI. (2023). ChatGPT Language Model. Dostupné z: https://openai.com/chatgpt [cit. 2025-5-8].

## Literatura:

InterviewBit. (2021–2023). Python Commands List. Dostupné z: https://www.interviewbit.com/blog/python-commands/ [cit. 2025-5-8].

