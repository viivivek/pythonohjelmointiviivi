while True:
    valinta = input("Valitse laskutoimitus (+, -, *, /) tai lopetus:")
    if valinta == "lopetus":
        break

    luku1 = float(input("Valitse ensimmäinen luku: "))
    luku2 = float(input("Valitse toinen luku: "))

    if valinta == "+":
        print("Tulos:", luku1 + luku2)
    elif valinta == "-":
        print("Tulos:", luku1 - luku2)
    elif valinta == "*":
        print("Tulos:", luku1 * luku2)
    elif valinta == "/":
        print("Tulos:", luku1 / luku2)






