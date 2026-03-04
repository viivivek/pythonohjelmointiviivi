nimi = input("Anna nimesi:")

if nimi == "Matti":
    print("Saat keiton ilmaiseksi!")

else:
    maara = int(input("Kuinka monta keittoannosta haluat?:"))
    hinta = 5.90
    kokonaishinta = hinta * maara
    print(kokonaishinta)
