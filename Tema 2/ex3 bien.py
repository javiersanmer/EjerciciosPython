print("¿Qué pista vas a alquilar?")
print("1.Tenis")
print("2.Futbol sala")
print("3.Futbol 11")
print("4.Rugby")

tipo = int(input("Introduce el tipo de pista: "))
dia = input("Introduce el día de la semana (L,M,X,J,V,S,D): ")
focos = input("¿Quieres focos (S/N): ")
alumno = input("¿Eres alumno/a de la UGR? (S/N): ")

precio = 0

if dia == "S" or dia == "D":
    es_finde = True
else: 
    es_finde = False

match tipo:
    case "1":
        precio = 10 if es_finde else 8 
        precio = precio + 5 if focos == "S" else precio
    case "2":
        precio = 30 if es_finde else 26
        precio = precio + 10 if focos == "S" else precio
    case "3":
        precio = 79 if es_finde else 64
        precio = precio + 20 if focos == "S" else precio
    case "4": 
        precio = 94 if es_finde else 80
        precio = precio + 25 if focos == "S" else precio


if alumno == "S":
    precio = precio * 0.85

print(f"Tienes que pagar {round(precio,2)} euros")