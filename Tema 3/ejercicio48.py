matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        if elemento < 0:
            matriz[i][j] *= -1
print(matriz)
