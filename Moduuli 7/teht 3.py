lentoasemat = {}
toiminnot = ("haku", "uusi", "lopeta")


while True:
    toiminto = input("Valitse toiminto:")

    if toiminto == "lopeta":
        break

    elif toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi on:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    else:
        print("Virheellinen toiminto.")