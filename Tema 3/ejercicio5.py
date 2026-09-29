import random
numeros = [random.randint(0,10) for _ in range(1000)] #Otra forma
minimo = numeros[0]

for numero in numeros:
    if numero < minimo:
        minimo = numero
print(minimo)