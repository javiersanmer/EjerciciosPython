import math
def longitudCirunferencia(longitudRadio: float) -> float:
    
    longitudCirc = 2 * longitudRadio * math.pi
    return longitudCirc

radio = float(input("Introduce la longitud del radio: "))

print(f"Tu longitud de circunferencia es {longitudCirunferencia(radio)}")