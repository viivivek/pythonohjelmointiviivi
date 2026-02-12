pituus = input("Mikä on kuhan pituus senttimetreinä?:")
pituus = float(pituus)
vahimmaismitta = 37

if pituus < vahimmaismitta:
    puuttuu = vahimmaismitta - pituus
    print(f"Kuha on alimittainen. Laske kala takaisin järveen")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")

else:
    print("Kuha on riittävän pitkä! Voit pitää saaliin.")