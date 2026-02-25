syote = input("Anna luku (tyhjä lopettaa): ")

if syote == "":
    print("Et syöttänyt lukuja.")
else:
    pienin = float(syote)
    suurin = float(syote)

    while True:
        syote = input("Anna luku (tyhjä lopettaa): ")
        if syote == "":
            break

        luku = float(syote)

        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    print("Pienin:", pienin)
    print("Suurin:", suurin)