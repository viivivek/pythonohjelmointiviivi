import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä: "))

luku = 0
while luku != maksimi:
    luku = noppa(maksimi)
    print(luku)