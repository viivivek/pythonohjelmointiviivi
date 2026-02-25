import random

salainen_luku = random.randint(1, 10)
arvaus = 0

while arvaus != salainen_luku:
    arvaus = int(input("Arvaa luku väliltä 1–10: "))

    if arvaus < salainen_luku:
        print("Liian pieni arvaus")
    elif arvaus > salainen_luku:
        print("Liian suuri arvaus")

print("Oikein")