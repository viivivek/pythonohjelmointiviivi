luvut = []

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)