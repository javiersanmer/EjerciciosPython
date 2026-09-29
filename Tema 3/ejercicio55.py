import random
def matrizAleatoria(n:int, m:int, a:int, b:int) -> list[list[int]]:
    matriz = []
    for _ in range(n):
        matriz.append([random.randint(a,b) for _ in range(m)])
    return matriz

resultado =matrizAleatoria(4,4,1,2)

print(resultado)