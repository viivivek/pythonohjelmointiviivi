def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def osamaara(a, b):
    if b == 0:
        return "Virhe (nollalla jako)"
    return a / b

while True:
    valinta = input("Valitse laskutoimitus (+, -, *, /) tai lopetus: ")
    if valinta == "lopetus":
        break

    a = float(input("Valitse ensimmäinen luku: "))
    b = float(input("Valitse toinen luku: "))

    if valinta == "+":
        print("Tulos:", a + b)
    elif valinta == "-":
        print("Tulos:", a - b)
    elif valinta == "*":
        print("Tulos:", a * b)
    elif valinta == "/":
        print("Tulos:", a / b)