# Výherní automat 🎰

Tento projekt obsahuje jednoduchou textovou implementaci výherního automatu v Pythonu. Hráč začíná se 100 Kč kreditem a cílem je získat výherní kombinace symbolů. Hra obsahuje několik různých výherních podmínek a útěchové výhry.

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
