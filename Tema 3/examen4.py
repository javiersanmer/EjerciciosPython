def generar_matriz(filas: int, columnas: int, inicial: int) -> list[list[int]]:
    matriz = []
    for _ in range(filas):
        filas = []
        for _ in range(columnas):
            filas.append(inicial)
            inicial += 1
        matriz.append(filas)
    return matriz
print(generar_matriz(4,4,5))
