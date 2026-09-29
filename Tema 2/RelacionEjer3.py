diaSem = input("Introduce el día de la semana: ")
tipoHab = input("Introduce el tipo de habitación: ")
festivo = input("Introduce el dia festivo: ")
tieneCupon = input("Tiene cupón?")

if tipoHab == "I":
    indiv = True
else:
    indiv = False

if diaSem == "V" or diaSem == "S" or festivo == "S":
    precio = 45 if indiv else 70
elif diaSem == "D" or festivo == "N":
    precio = 40 if indiv else 60
else:
    precio = 30 if indiv else 50

if tieneCupon == "S":
    cupon = int(input("Introduce el cupon entre 0 y 100: "))

    if cupon > 0 or cupon <= 100:
        precio = precio * (1-(cupon/100))

print(round(precio,2))











#el ultimo ejercicio del examen es con módulos