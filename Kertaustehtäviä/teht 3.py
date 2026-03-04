import math

luku = int(input("Anna kokonaisluku: "))

while luku != 0:

    if luku < 0:
        print("Virheellinen numero")
    else:
        print("Luvun neliöjuuri on", math.sqrt(luku))

    luku = int(input("Anna kokonaisluku: "))

print("Ohjelma lopetettu.")