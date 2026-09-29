longitud1 = float(input("Introduce la longitud: "))
longitud2 = float(input("Introduce la longitud: "))
longitud3 = float(input("Introduce la longitud: "))

if longitud1 == longitud2 == longitud3:
    print("Equilatero")
elif longitud1 == longitud2 or longitud1 == longitud3:
    print("Isósceles")
else:
    print("Escaleno")