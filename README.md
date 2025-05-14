# 🎰 Výherní automat v Pythonu

Tato textová hra simuluje jednoduchý výherní automat (slot machine). Hráč začíná se 100 Kč kreditem a za každé zatočení utratí 10 Kč. Cílem je vytočit výherní kombinace symbolů a získat kredit zpět.

## 🧠 Jak hra funguje

- 💰 Každé zatočení stojí 10 Kč
- 🎉 **3 stejné symboly** = výhra 50 Kč
- 🙂 **2 stejné vedle sebe** = výhra 15 Kč
- 🔄 **3 různé symboly 3x za sebou** = útěchová výhra 5 Kč
- ❌ Při jiné kombinaci nic nevyhráváš

## ▶️ Spuštění hry

1. Ujisti se, že máš nainstalovaný Python (doporučena verze 3.6+)
2. Ulož kód do souboru, např. `automaty.py`
3. Spusť skript v terminálu:

```bash
python automaty.py
