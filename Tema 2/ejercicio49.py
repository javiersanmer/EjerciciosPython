import random
import math

inicio = int(input("Introduce un inicio: "))
fin = int(input("Introduce un fin: "))
nVeces = int(input("Inserta la cantidad dde números aleatorios a generar: "))

rangoIni = fin - inicio

for inicio in range(nVeces):
    sol = math.floor(inicio + rangoIni *random.random())
    print(sol)