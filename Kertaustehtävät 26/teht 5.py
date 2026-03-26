def suurin_arvo(luku1, luku2, luku3):
    tulos = max(luku1, luku2, luku3)
    return tulos

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

suurin = suurin_arvo(luku1, luku2, luku3)
print(suurin)