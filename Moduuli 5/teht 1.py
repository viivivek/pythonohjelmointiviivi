import random

maara = int(input("Kuinka monta arpakuutiota heitetään?: "))

summa = 0

for i in range(maara):
    silmaluku = random.randint(1, 6)
    print("Nopan", i + 1, "tulos:", silmaluku)
    summa += silmaluku

print("Silmälukujen summa on:", summa)