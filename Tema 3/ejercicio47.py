matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]
posF= posC = None
encontrado = False

#devolviendo el primer 5
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        if elemento == 5:
            posF = i
            posC = j
print(f"El número 5 se encuentra en las fila {posF} y columna {posC}")

posF= posC = None

#delvolviendo el último 5
for i, fila in enumerate(matriz):
    if encontrado:
        break
    for j, elemento in enumerate(fila):
        if elemento == 5:
            posF = i
            posC = j
            encontrado = True
            break #Así devuelve la pos del primero no del último
print(f"El número 5 se encuentra en las fila {posF} y columna {posC}")

posF= posC = None

#usando .index encontrado el ultimo
for i, fila in enumerate(matriz):
    if fila.count(5) > 0:
        posF = i
        posC = fila.index(5)

print(f"El número 5 se encuentra en las fila {posF} y columna {posC}")

#usando .index encontrado el primero
for i, fila in enumerate(matriz):
    if fila.count(5) > 0:
        posF = i
        posC = fila.index(5)
        break