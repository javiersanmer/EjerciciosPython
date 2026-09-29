from random import randint
def matrizAleatoria(n: int,m: int) -> list[list[int]]:
   matriz = []

   for _ in range(n):
      matriz.append([randint(0,9) for _ in range(m)])
   return matriz
def imprimirMatriz(m:list[list[int]]) -> None:
   for fila in m:
      for n in fila:
         print(n, end = " ")
      print()
nFila = int(input("Pon filas "))
nColuma= int(input("Pon columna "))

imprimirMatriz(matrizAleatoria(nFila,nColuma))


#POSIBLE EJERCICIO HACER ESTO PERO FORMANDO CUADRADO O ALGO