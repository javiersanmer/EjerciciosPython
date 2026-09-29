print("¿Qué pista vas a alquilar?")
print("1.Tenis")
print("2.Futbol sala")
print("3.Futbol 11")
print("4.Rugby")

tipoPista = int(input("Introduce el tipo de pista: "))
diaSem = input("Introduce el día de la semana (L,M,X,J,V,S,D): ")
focos = input("¿Quieres focos (S/N): ")
alumno = input("¿Eres alumno/a de la UGR? (S/N): ")

if diaSem == "L" or diaSem == "M" or diaSem == "X" or diaSem == "J" or diaSem == "V":
    entreSemana = diaSem

if tipoPista == 1:
    if diaSem == entreSemana:
        precio = 8
    elif diaSem == "S" or diaSem == "D":
        precio = 10
if tipoPista == 2:
    if diaSem == entreSemana:
        precio = 26
    elif diaSem == "S" or diaSem == "D":
        precio = 30
if tipoPista == 3:
    if diaSem == entreSemana:
        precio = 64
    elif diaSem == "S" or diaSem == "D":
        precio = 79
if tipoPista == 4:
    if diaSem == entreSemana:
        precio = 80
    elif diaSem == "S" or diaSem == "D":
        precio = 94

if focos == "S":
    if tipoPista == 1:
        precio = precio + 5
    elif tipoPista == 2:
        precio = precio + 10
    elif tipoPista == 3:
        precio = precio +20
    elif tipoPista == 4:
        precio = precio + 25

if alumno == "S":
    precio = precio * 0.85

precio = round(precio,2)
print(f"Tienes que pagar {precio} euros")



