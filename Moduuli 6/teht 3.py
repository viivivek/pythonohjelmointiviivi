def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    maara = float(input("Mikä on bensiinin määrä galloonina?: "))
    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print("Litroina:", litrat)


