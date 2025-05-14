#  Výherní automat v Pythonu

Tato textová hra simuluje jednoduchý výherní automat (slot machine). Hráč začíná se 100 Kč kreditem a za každé zatočení utratí 10 Kč. Cílem je vytočit výherní kombinace symbolů a získat kredit zpět.

## Jak hra funguje

-  Každé zatočení stojí 10 Kč
-  **3 stejné symboly** = výhra 50 Kč
-  **2 stejné vedle sebe** = výhra 15 Kč
-  **3 různé symboly 3x za sebou** = útěchová výhra 5 Kč
-  Při jiné kombinaci nic nevyhráváš

## ▶️ Spuštění hry

1. Ujisti se, že máš nainstalovaný Python (doporučena verze 3.6+)
2. Ulož kód do souboru, např. `automaty.py`
3. Spusť skript v terminálu:

```bash
python automaty.py

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
Pro náhodný výběr symbolů

⚙️ Inicializace proměnných
python
symboly = ["🍺","🍷","🍸","🍹","🍑","🍆"]
kredit = 100
pocet_3_ruzne_za_sebou = 0
🎯 Hlavní herní smyčka
python
while kredit >= 10:
    input("Stiskni ENTER pro zatočení...")
    kredit -= 10
    # Generování a vyhodnocení výsledku by následovalo
🔧 Instalace a spuštění
Požadavky:

Python 3.x

Spuštění:

bash
git clone https://github.com/vase-repo/vherni-automat.git
cd vherni-automat
python slot_machine.py
🚀 Možná rozšíření
Přidání různých výherních kombinací

Bonusová kola

Možnost volby sázky

Grafické rozhraní (PyGame)

Ukládání nejvyššího skóre

📜 Licence
Tento projekt je licencován pod licencí MIT - viz soubor LICENSE pro detaily.

Note: Tento projekt byl vytvořen pro vzdělávací účely. Gamblerství může být návykové, hrajte zodpovědně.


Tento README.md obsahuje všechny důležité části pro GitHub repozitář:
- Štítky s verzí Pythonu a licencí
- Přehlednou strukturu s anotovanými odkazy
- Podrobný popis kódu včetně ukázek
- Návod k instalaci a spuštění
- Nápady na rozšíření
- Varování před gamblingem

Formátování využívá standardní GitHub Markdown syntax včetně:
- Nadpisů různých úrovní
- Seznamů
- Kódových bloků s syntax highlighting
- Emoji pro lepší vizuální orientaci
- Poznámkového bloku na konci
