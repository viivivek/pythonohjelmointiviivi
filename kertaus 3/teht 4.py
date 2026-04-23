import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    ero_x = x2 - x1
    ero_y = y2 - y1
    etaisyys = math.sqrt(ero_x ** 2 + ero_y ** 2)

    return etaisyys

print("Anna ensimmäisen pisteen koordinaatit:")
x1_input = float(input("x1: "))
y1_input = float(input("y1: "))
piste1 = create_point(x1_input, y1_input)

print("\nAnna toisen pisteen koordinaatit:")
x2_input = float(input("x2: "))
y2_input = float(input("y2: "))
piste2 = create_point(x2_input, y2_input)

tulos = distance(piste1, piste2)

print(f"\nPisteiden {piste1} ja {piste2} välinen etäisyys on {tulos:.2f}")

