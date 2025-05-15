import random

symboly = ["🍺","🍷","🍸","🍹","🍑","🍆"]
kredit = 100
pocet_3_ruzne_za_sebou = 0

print("🎰 Vítej ve výherním automatu!")
print("Za každé zatočení zaplatíš 10 Kč. Pokud padnou 3 stejné symboly, vyhráváš 50 Kč.")
print("--------------------------------------------------")

while kredit >= 10:
    input("Stiskni ENTER pro zatočení...")
    kredit -= 10

    tah = [random.choice(symboly) for _ in range(3)]
    print(" | ".join(tah))

    if tah[0] == tah[1] == tah[2]:
        print("🎉 Jackpot! 3 stejné symboly! Vyhráváš 50 Kč!")
        kredit += 50
        pocet_3_ruzne_za_sebou = 0
    elif tah[0] == tah[1] or tah[1] == tah[2] or tah[0]==tah[2]:
        print(" Dvě stejné vedle sebe! Vyhráváš 15 Kč!")
        kredit += 15
        pocet_3_ruzne_za_sebou = 0
    elif len(set(tah)) == 3:
        pocet_3_ruzne_za_sebou += 1
        print(f" 3 různé symboly ({pocet_3_ruzne_za_sebou}x za sebou)")

        if pocet_3_ruzne_za_sebou == 3:
            print("🎁 Útěcha! 3 různé padly 3x za sebou – dostáváš 5 Kč!")
            kredit += 5
            pocet_3_ruzne_za_sebou = 0
    else:
        print("❌ Nic jsi nevyhrál.")
        pocet_3_ruzne_za_sebou = 0

    print(f"Zbývá ti {kredit} Kč.\n")

    if kredit < 10:
        print(" Nemáš dost peněz na další hru. Konec.")
        break

    pokracovat = input("Chceš pokračovat? (ano(a)/ne(n)): ").lower()
    if pokracovat != "a":
        print("Díky za hru!")
        break

