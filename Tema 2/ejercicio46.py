import math
while True:
    a = float(input("Inserta el termino a: "))
    if a == 0:
        break
    b = float(input("Inserta el termino b: "))
    c = float(input("Inserta el termino c: "))

    sol1 = (-b+math.sqrt(b*b-4*a*c))/2*a
    sol2 = (-b-math.sqrt(b*b-4*a*c))/2*a

    print(sol1)
    print(sol2)