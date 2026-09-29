from random import randint
aleatorios = [randint(0,100) for _ in range(20)]
aleatoriosCondicion = [num for num in aleatorios if num % 5 == 0]
print(aleatoriosCondicion)