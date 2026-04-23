henkilot = {"John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]}

print(f"Johnin nimi: {henkilot['John'][0]}, ikä: {henkilot['John'][1]}")
print(f"Emilyn ammatti: {henkilot['Emily'][2]}")

henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]

henkilot["Sophia"] = ["Sophia", 35, "Doctor"]

del henkilot["Emily"]

print("\nLopullinen sanakirja:")
print(henkilot)