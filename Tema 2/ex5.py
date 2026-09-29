import random

i= 2
par = False
es_par = 0

eleccion = input("¿Qué eliges (pares o nones)?: ")

while eleccion != "pares" and eleccion != "nones":
    eleccion = input("Elección no válida. Elige entre pares o nones: ")

sacaH = int(input("¿Cuantos dedos sacas?: "))

while sacaH < 0 or sacaH > 11:
    sacaH = int(input("Numero de dedos no válido (entre 0 y 10): "))

sacaM = random.randint(0,10)

suma = sacaH + sacaM
esPar = suma % 2 == 0

if esPar == 0:
    par = True

print(f"Has sacado {sacaH} y la máquina {sacaM}")
if (eleccion == "pares" and par) or (eleccion == "nones" and not par):
    print(f"Has perdido")
else:
    print(f"Has ganado")


'''si empre quen hay que ahcer algo de pedir un dato y hacerlo hasta que que no lo metan bien no se para se usa wihle ture'''
