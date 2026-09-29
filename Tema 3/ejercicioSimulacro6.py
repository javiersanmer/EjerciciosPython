def esCuadrada(m:list) -> bool:
    return len(m) == len(m[0])
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3],
    [4, 5, 6]
]

esCuadrada(m1)
esCuadrada(m2)