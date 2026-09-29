import random

def crear_tablero():
    return [[" " for _ in range(10)] for _ in range(10)]

def colocar_barco(tablero, tamaño):
    colocado = False
    while not colocado:
        orientacion = random.choice(["H", "V"])
        fila = random.randint(0, 9)
        col = random.randint(0, 9)

        if orientacion == "H":
            if col + tamaño <= 10:
                libre = True
                for c in range(col, col+tamaño):
                    if tablero[fila][c] != "~":
                        libre = False
                if libre:
                    for c in range(col, col+tamaño):
                        tablero[fila][c] = "B"
                    colocado = True

        else:
            if fila + tamaño <= 10:
                libre = True
                for f in range(fila, fila+tamaño):
                    if tablero[f][col] != "~":
                        libre = False
                if libre:
                    for f in range(fila, fila+tamaño):
                        tablero[f][col] = "B"
                    colocado = True


def colocar_flota(tablero):
    barcos = [
        5,
        4, 4,
        3, 3, 
        3, 3,
        2, 2, 
        1 
    ]
    for tam in barcos:
        colocar_barco(tablero, tam)

def imprimir_tablero_disparos(tablero):
    print("    A B C D E F G H I J")
    print("    --------------------")
    for i, fila in enumerate(tablero):
        linea = f"{i+1:2} | "
        for casilla in fila:
            if casilla in ("1", "O"):
                linea += casilla + " "
            else:
                linea += "~ "
        print(linea)

def es_numero_valido(texto):
    if len(texto) == 0:
        return False
    for c in texto:
        if c not in "0123456789":
            return False
    return True

def quitar_espacios(texto):
    resultado = ""
    for c in texto:
        if c != " ":
            resultado += c
    return resultado

def traducir_coordenada(coord):
    letras = "ABCDEFGHIJ"

    coord = coord.upper()
    coord = quitar_espacios(coord)

    if len(coord) < 2 or len(coord) > 3:
        return None, None

    letra = coord[0]
    numero = coord[1:]

    if letra not in letras:
        return None, None

    if not es_numero_valido(numero):
        return None, None

    num = int(numero)
    if num < 1 or num > 10:
        return None, None

    fila = num - 1
    col = letras.index(letra)
    return fila, col

def todos_hundidos(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "B":
                return False
    return True

def hundir_la_flota():
    print(" HUNDIR LA FLOTA - MODO SOLITARIO ")
    print("1) Fácil (80 misiles)")
    print("2) Normal (60 misiles)")
    print("3) Difícil (40 misiles)")

    dif = input("Elige dificultad (1-3): ")

    if dif == "1":
        misiles = 80
    elif dif == "2":
        misiles = 60
    else:
        misiles = 40

    enemigo = crear_tablero()
    disparos = crear_tablero()
    colocar_flota(enemigo)

    print("\npon coordenadas como: A3")

    while misiles > 0:
        imprimir_tablero_disparos(disparos)
        print(f"\nMisiles restantes: {misiles}")

        coord = input("Dispara a: ")

        fila, col = traducir_coordenada(coord)

        if fila is None:
            print(" Ahi no se puede.\n")
        else:
            if disparos[fila][col] != "~":
                print("Ahi no era maquina\n")
            else:
                misiles -= 1
                if enemigo[fila][col] == "B":
                    print("Auuuch\n")
                    disparos[fila][col] = "X"
                    enemigo[fila][col] = "X"
                else:
                    print("Agua\n")
                    disparos[fila][col] = "O"

                if todos_hundidos(enemigo):
                    print("Has hundido toda la flota ¡MAQUINON!")
                    imprimir_tablero_disparos(disparos)
                    return

    print("\nTe has quedado sin misiles. Eres un looser.")





from random import randint, choice

def generaTablero():
    return [[" " for _ in range(10)] for _ in range(10)]

def menuJuego(opcionMenu: int):
    print("Elige la dificultad: ")
    print("1. Modo fácil: 80 misiles")
    print("2. Modo normal: 60 misiles")
    print("3. Modo fácil: 40 misiles")

    opcionMenu = int("Elige una opción: ")
    if opcionMenu == 1:
        misiles = 80
    elif opcionMenu == 2:
        misiles = 60
    elif opcionMenu == 3:
        misiles = 40

def imprimir_tablero_disparos(tablero):
    print("    A B C D E F G H I J")
    print("    --------------------")
    for i, fila in enumerate(tablero):
        linea = f"{i+1:2} | "
        for casilla in fila:
            if casilla in ("1", "O"):
                linea += casilla + " "
            else:
                linea += " "
        print(linea)

def cocolarBarco():
    colado = False
    


def generaTablero():
    return [[" " for _ in range(10)] for _ in range(10)]


def eligeMenu(opcionMenu):
    opcionMenu = int(input("Que quieres hacer: "))
    print("1. Jugar")
    print("2. Elegir dificultad")

    if opcionMenu == 1:
        pass
    elif opcionMenu == 2:
        cambiarDificultad = int(input("Ingresa la dificultad: "))
        while cambiarDificultad != 0:       

            if cambiarDificultad == 1:
                misiles = 80
            elif cambiarDificultad == 2:
                misiles = 60
            elif cambiarDificultad == 3:
                misiles = 40
            else:
                break

def colocar_flota(tablero):
    flota = {5: 1, 4: 2, 3: 4, 2: 2, 1: 1}
    for tam, cantidad in flota.items():
        for _ in range(cantidad):
            colocar_barco(tablero, tam)

def imprimir_tablero_disparos(tablero):
    print("    A B C D E F G H I J")
    print("    --------------------")
    for i, fila in enumerate(tablero):
        linea = f"{i+1:2} | "
        for casilla in fila:
            if casilla in ("1", "O"):
                linea += casilla + " "
            else:
                linea += " "
        print(linea)


