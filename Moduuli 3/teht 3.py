sukupuoli = input("Anna biologinen sukupuoli (nainen, mies): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Naisen hemoglobiiniarvo on alhainen.")

    elif 117 <= hemoglobiini <= 175:
        print("Naisen hemoglobiinarvo on normaali.")

    else:
        print("Naisen hemoglobiiniarvo on korkea.")

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Mies hemoglobiiniarvo on alhainen.")

    elif 134 <= hemoglobiini <= 195:
        print("Mies hemoglobiiniarvo on normaali.")

    else:
        print("Mies hemoglobiiniarvo on korkea.")
