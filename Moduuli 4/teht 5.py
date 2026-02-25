Oikea_tunnus = "python"
Oikea_salasana = "rules"

yritykset = 0
maksimi_yritykset = 5

while yritykset < maksimi_yritykset:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == Oikea_tunnus and salasana == Oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {maksimi_yritykset - yritykset}")

if yritykset == maksimi_yritykset:
    print("Pääsy evätty")