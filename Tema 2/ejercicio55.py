import math
def hipotenusa(c1 : float, c2 : float) -> float:
    h = math.sqrt(c1*c1 + c2*c2)
    return h

c1 = float(input("Introduce c1: "))
c2 = float(input("Introduce c2: "))
print(f"El resultado de h es: {hipotenusa(c1,c2)}")