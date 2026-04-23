kirjasto = {"Tuntematon sotilas": ["Väinö Linna", 1954, "Sotaromaani"],
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "Historiallinen romaani"],
    "Harry Potter ja viisasten kivi": ["J.K. Rowling", 1997, "Fantasia"]}

print(f"Sinuhen kirjoittaja: {kirjasto['Sinuhe egyptiläinen'][0]}")
print(f"Harry Potterin genre: {kirjasto['Harry Potter ja viisasten kivi'][2]}")

kirjasto["Tuntematon sotilas"][2] = "Klassikko"

kirjasto["Puhdistus"] = ["Sofi Oksanen", 2008, "Draama"]

del kirjasto["Sinuhe egyptiläinen"]

print("\nPäivitetty kirjasto:")
for kirja, tiedot in kirjasto.items():
    print(f"Kirja: {kirja} | Tiedot: {tiedot}")