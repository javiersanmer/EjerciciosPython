import random
import math

inicio = int(input("Introduce un inicio: "))
fin = int(input("Introduce un fin: "))
nVeces = int(input("Inserta la cantidad dde números aleatorios a generar: "))

for i in range(nVeces):
    sol = random.randint(inicio,fin)
    print(sol)