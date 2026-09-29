import random
numPar = 0
numImpar = 0
contador = 0
for i in range(10):
    num = random.randint(20,40)
    print(num)

    if num % 2 == 0:
        numPar += 1

porcentajePar = numPar/10 * 100 #10 pq es el range
porcentajeImpar =100 - porcentajePar 
print(f"El porcentaje de par : {porcentajePar}")
print(f"El porcentaje de impar : {porcentajeImpar}")


