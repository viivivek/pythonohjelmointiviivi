import math

def pizzan_hinta_per_m2(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade / 100) ** 2
    return hinta / pinta_ala

h1 = float(input("1. pizzan halkaisija (cm): "))
p1 = float(input("1. pizzan hinta (€): "))

h2 = float(input("2. pizzan halkaisija (cm): "))
p2 = float(input("2. pizzan hinta (€): "))

y1 = pizzan_hinta_per_m2(h1, p1)
y2 = pizzan_hinta_per_m2(h2, p2)

print("")

print("1. pizza:", round(y1, 2), "€/m²")
print("2. pizza:", round(y2, 2), "€/m²")

if y1 < y2:
    print("Eka pizza on parempi diili")
elif y2 < y1:
    print("Toka pizza on parempi diili")
else:
    print("Samat hinnat per pinta-ala")