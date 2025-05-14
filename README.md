# 🎰 Výherní Automat v Pythonu

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Jednoduchá textová implementace výherního automatu napsaná v Pythonu.

## 📋 Obsah
- [Popis hry](#-popis-hry)
- [Jak hrát](#-jak-hrát)
- [Struktura kódu](#-struktura-kódu)
- [Instalace a spuštění](#-instalace-a-spuštění)
- [Možná rozšíření](#-možná-rozšíření)
- [Licence](#-licence)

## 🎮 Popis hry
Hráč začíná s kreditem **100 Kč**. Každé zatočení stojí **10 Kč**. Pokud se objeví **3 stejné symboly** vedle sebe, hráč vyhrává **50 Kč**.

**Používané symboly:**
- 🍺 (pivo)
- 🍷 (víno)
- 🍸 (koktejl)
- 🍹 (tropický drink)
- 🍑 (broskev)
- � (lilek)

## 🕹️ Jak hrát
1. Spusťte program
2. Stiskněte `ENTER` pro zatočení
3. Každé zatočení odečte 10 Kč z kreditu
4. Při výhře (3 stejné symboly) získáte 50 Kč
5. Hra končí, když kredit klesne pod 10 Kč

## 💻 Struktura kódu

### 📚 Importované knihovny
```python
import random
```
#Inicializace proměnných
```
symboly = ["🍺","🍷","🍸","🍹","🍑","🍆"]
kredit = 100
pocet_3_ruzne_za_sebou = 0
```

#Hlavní herní smyčka
```
while kredit >= 10:
    input("Stiskni ENTER pro zatočení...")
    kredit -= 10
    # Generování a vyhodnocení výsledku by následovalo
```

