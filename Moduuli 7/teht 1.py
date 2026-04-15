vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("Anna kuukauden numero järjestysnumero (1-12): "))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print("Vuodenaika on", vuodenajat[3])
elif kuukausi >= 3 and kuukausi <= 5:
    print("Vuodenaika on", vuodenajat[0])
elif kuukausi >= 6 and kuukausi <= 8:
    print("Vuodenaika on", vuodenajat[1])
elif kuukausi >= 9 and kuukausi <= 11:
    print("Vuodenaika on", vuodenajat[2])