import random
import math

inicio = float(input("Introduce un inicio: "))
fin = float(input("Introduce un fin: "))
nVeces = int(input("Inserta la cantidad dde números aleatorios a generar: "))

rangoIni = (fin - inicio) 

for inicio in range(nVeces):
    sol = round(inicio + random.random() * rangoIni ,2)
    print(sol)
    