def dimension(matriz: list[list[int]]) -> list[int]:
    if len(matriz) == 0:
        return [0, 0]
    else:
        return [len(matriz), len(matriz[0])] #len(matriz) num filas, len(matriz[0] num de columnas)

print(dimension([[1,2,3], [3,4,5]]))