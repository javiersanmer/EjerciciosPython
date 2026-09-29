longitud1 = int(input("Introduce la longitud: "))
longitud2 = int(input("Introduce la longitud: "))
longitud3 = int(input("Introduce la longitud: "))

if (longitud1 + longitud2 > longitud3) and (longitud2 + longitud3 > longitud1) and+ (longitud3 + longitud2 > longitud3):
    print("Triángulo válido")
else:
    print("Triángulo no válido")