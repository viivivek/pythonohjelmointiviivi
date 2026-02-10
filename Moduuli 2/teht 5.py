leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
kokonais_luodit = luodit + (naulat * 32) + (leiviskat * 20 * 32)
grammat_yhteensa = kokonais_luodit * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print("\nMassa nykymittojen mukaan:")
print(str(kilogrammat) + " kilogrammaa ja " + str(round(grammat, 2)) + " grammaa.")
