from random import randint
def pedirCoordenada(mensaje: str,inicio: int, final: int) -> int:
    while True:
        coord = int(input(mensaje))

        if coord >=inicio and coord <=final:
            break
        else:
            print("Número fuera de rango")
    return coord

def generarCoordenada(pos: int) -> tuple:
    return (pos // 3, pos % 3)

def imprimirtablero(tablero: list[list[int]]):
    for fila in tablero:
        for casilla in fila:
            signo = "-"
            if casilla == 1:
                signo = "X"
            elif casilla == -1:
                signo = "O"
            print(signo, end=" ")
        print("")

def insertarJugada(tablero: list[list[int]]):
    fila = pedirCoordenada("Inserta una fila", 0, 2)
    columna = pedirCoordenada("Inserta una columna", 0, 2)
    
    while tablero[fila][columna] != 0: #mientras la pos esté ocupada
        print("La posición ya está ocupada")
        fila = pedirCoordenada("Inserta una fila: ", 0, 2)
        columna = pedirCoordenada("Inserta una columna: ", 0, 2)
    tablero[fila][columna] = 1

def ia(tablero: list[list[int]]):
    fila, columna = generarCoordenada(randint(0, 8))
    
    while tablero[fila][columna] != 0: #mientras la pos esté ocupada
        fila, columna = generarCoordenada(randint(0, 8))
    
    tablero[fila][columna] = -1

def resumen(tablero: list[list[int]]) -> tuple[int]:
    return (sum(tablero[0]), 
            sum(tablero[1]),
            sum(tablero[2]),
            sum((tablero[0][0], tablero[1][0], tablero[2][0])),
            sum((tablero[1][1], tablero[1][0], tablero[0][1])),
            sum((tablero[2][2], tablero[2][1], tablero[2][2])),
            sum((tablero[0][0], tablero[1][1], tablero[2][2])),
            sum((tablero[0][2], tablero[1][1], tablero[2][0])))
    
#devuelve 1 si ha ganado, -1 si pierde y 0 si la partida continúa
def estado(tablero: list[list[int]]) -> int:
    datos_resumen = resumen(tablero)
    if max(datos_resumen) == 3:
        return 1
    elif min(datos_resumen) == -3:
        return -1
    else:
        return 0

