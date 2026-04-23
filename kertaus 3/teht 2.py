oppilaat = {"Viivi": ["Viivi", 8, "Kuvataide"],
    "Sanni": ["Sanni", 7, "Matematiikka"],
    "Elias": ["Elias", 9, "Historia"]}

print(f"Viivin vuosiluokka: {oppilaat['Viivi'][1]}")
print(f"Sannin lempiaine: {oppilaat['Sanni'][2]}")

oppilaat["Elias"][2] = "Liikunta"

oppilaat["Aada"] = ["Aada", 8, "Musiikki"]

del oppilaat["Elias"]

print("\nPäivitetty sanakirja:")
for nimi, tiedot in oppilaat.items():
    print(f"{nimi}: {tiedot}")