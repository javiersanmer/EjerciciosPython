def obtenerColumna(m: list[list[int]], c: int) -> list[int]:
    columna = []
    for fila in m:
        columna.append(fila[c])
    return columna

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(obtenerColumna(matriz, 1))