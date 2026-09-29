sabores = ["Fresa", "Melocoton", "Arandanos", "Naranja", "Frambuesa", "Mango", "Ciruela", "Albaricoque", "Higo", "Kiwi"]
precios = [2.40, 2.85, 3.10, 2.20, 3.50, 2.95, 2.60, 2.75, 3.00, 2.30]
es_sin_azucar = [False, False, True, False, True, False, False, False, True, False]

apartadoA = [nombre for i, nombre in enumerate(sabores) if len(nombre) % 2 == 1 and es_sin_azucar[i]]
print(apartadoA)

apartadoB = []
for i, precio in enumerate(precios):
    if max(precios) == precio:
        apartadoB.append(sabores[i])
    if min(precios) == precio:
        apartadoB.append(sabores[i])
print(apartadoB)

def generar_matriz_indices(filas: int, columnas: int) -> list[list[int]]:
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = i + j
            fila.append(valor)
        matriz.append(fila)
    return matriz

print(generar_matriz_indices(3, 4))

def generar_matriz_suma(filas: int, columnas: int, inicio: int, salto: int) -> list[list[int]]:
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(inicio)
            inicio += salto
        matriz.append(fila)
    return matriz

print(generar_matriz_suma(3, 4, 2, 3))


def sumar_columna(m: list[list[int]], c: int) -> int:
    resul = 0
    for fila in m:
        resul += fila[c]
    return resul
    
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sumar_columna(matriz, 0))

def obtener_diagonal(m: list[list[int]], secundaria: bool) -> list[int]:
    diagonal = []
    n = len(m)

    for i in range(n):
        if secundaria:
            diagonal.append(m[i][n - 1 - i])
        else:
            diagonal.append(m[i][i])

    return diagonal

matriz = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

print(obtener_diagonal(matriz, True))

def paresConsecutivos(m: list[list[int]]) -> list[tuple[int,int]]:
    pares = []
    for fila in m:
        for i in range(len(fila) - 1):
            if fila[i+1] - fila[i] == 1:
                pares.append((fila[i], fila[i+1]))
    return pares

matriz = [
    [3, 4, 7, 8],
    [1, 2, 5, 6],
    [10, 12, 13, 14]
]

print(paresConsecutivos(matriz))
# Salida: [(3, 4), (7, 8), (1, 2), (5, 6), (12, 13), (13, 14)]


def obtener_fila_maxima(m: list[list[int]]) -> list[int]:
    filaMax = m[0]
    for fila in m:
        if sum(fila) > sum(filaMax):
            filaMax = fila
    return filaMax
matriz = [
    [2, 5, 1],
    [4, 0, 3],
    [1, 7, 2]
]

print(obtener_fila_maxima(matriz))

def contar_mayores(m: list[list[int]], valor: int) -> int:
    resul = 0
    for fila in m:
        for columna in fila:
            if columna > valor:
                resul += 1
    return resul

matriz = [
    [2, 5, 8],
    [1, 6, 3],
    [9, 4, 7]
]

print(contar_mayores(matriz, 5))

def cuenta_palabras(txt: str) -> list[tuple[str, int]]:
    palabras = txt.split()
    resultado = []
    
    for palabra in palabras:
        if palabra not in [p for p, _ in resultado]:
            nVeces = palabras.count(palabra)
            resultado.append((palabra, nVeces))
    return resultado

def imprimir_reporte(resultado:  list[tuple[str, int]]) -> list[tuple[str, int]]:
    for resu in resultado:
        print(f"Palabra:{resu[0]} n veces: {resu[1]}")



texto_quijote = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua rocín flaco y galgo corredor'
imprimir_reporte(cuenta_palabras(texto_quijote))


pedrolos = [
    ["Cuarzo",     2.65, False],
    ["Pirita",     5.02, False],
    ["Hematita",   5.26, False],
    ["Galena",     7.6,  False],
    ["Fluorita",   3.18, False],
    ["Calcita",    2.71, False],
    ["Magnetita",  5.17, True ],
    ["Malaquita",  3.9,  False],
    ["Obsidiana",  2.4,  False],
    ["Apatito",    3.2,  False]
]

apartadoA = [pedrolo[0] for pedrolo in pedrolos if len(pedrolo[0]) <= 7 and pedrolo[0][-1] != "a"]
print(apartadoA)
suma = 0
for numero in pedrolos:
    suma += numero[1]
media = suma / len(pedrolos)    

apartadoB = [pedrolo[0] for pedrolo in pedrolos if pedrolo[1] > media and not pedrolo[2]]
print(apartadoB)

apartadoC = [pedrolo[0] for pedrolo in pedrolos if ("p" in pedrolo[0].lower() or "t" in pedrolo[0].lower()) and not ("p" in pedrolo[0].lower() and "t" in pedrolo[0])]
print(apartadoC)

apartadoD = [pedrolo[0] for pedrolo in pedrolos if len(pedrolo[0]) % 2 == 1 and pedrolo[2]]

print(apartadoD)



def obtenerColumna(m: list[list[int]], c: int):
    columna = []
    for fila in m:
        columna.append(fila[c])
    return columna


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#5 ejercicios mermeladas y 2 adjedrez


#ADJEDREZ

def generar_tablero() -> list[list[str]]:
    tablero = []

    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(".")
        tablero.append(fila)

    return tablero

tablero = generar_tablero()

for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()


#BUSCAR UNA PIEZA
for i in range(8):
    for j in range(8):
        if tablero[i][j] == "R":
            ...
             
#RECCORER EN LÍNEA TORRE
while 0 <= f < 8 and 0 <= c < 8:
    if tablero[f][c] != ".":
        break
    f += df
    c += dc


#MOVIMIENTOS DE UNA TORRE

tablero = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "T", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]

fila_torre = 3
col_torre = 3

# Movimientos horizontales
for c in range(8):
    if c != col_torre:
        print((fila_torre, c))

# Movimientos verticales
for f in range(8):
    if f != fila_torre:
        print((f, col_torre))

#MUESTRA X
# Horizontal
for c in range(8):
    if c != col_torre:
        tablero[fila_torre][c] = "x"

# Vertical
for f in range(8):
    if f != fila_torre:
        tablero[f][col_torre] = "x"

for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()

#REY EN JAQUE

def rey_en_jaque(tablero: list[list[str]]) -> bool:
    rey_fila = -1
    rey_col = -1

    # 1. Buscar al rey
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    # 2. Direcciones diagonales
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 3. Para cada alfil, comprobar diagonales
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "A":
                for df, dc in direcciones:
                    f = i + df
                    c = j + dc

                    while 0 <= f < 8 and 0 <= c < 8:
                        if tablero[f][c] == "R":
                            return True
                        if tablero[f][c] != ".":
                            break
                        f += df
                        c += dc

    return False
tablero = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "A", ".", ".", ".", ".", "."],
    [".", ".", ".", "R", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]

print(rey_en_jaque(tablero))