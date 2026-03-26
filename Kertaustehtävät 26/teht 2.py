lista = []

while True:
    luku = int(input("Anna luku: "))

    if luku == 0:
        break

    lista.append(luku)

    print("Lisäysjärjestys:", lista)
    print("Suuruusjärjestys:", sorted(lista))
