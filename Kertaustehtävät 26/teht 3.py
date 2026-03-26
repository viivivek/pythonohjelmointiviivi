sanat =["kissa","koira","käärme","kani","lehmä"]

laskuri = 0

for sanat in sanat:
    if len(sanat) > 5:
        laskuri += 1

print("Sanoja, joissa on yli 5 kirjainta:", laskuri)


