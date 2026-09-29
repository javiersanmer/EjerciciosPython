# Generar tablero vacío
def generar_tablero() -> list[list[str]]:
    return [["." for _ in range(8)] for _ in range(8)]

# Crear un tablero de ajedrez 8x8
tablero = []

for fila in range(8):
    fila_tablero = []
    for columna in range(8):
        # Si la suma de fila y columna es par, la casilla es blanca (0), si no negra (1)
        if (fila + columna) % 2 == 0:
            fila_tablero.append(0)
        else:
            fila_tablero.append(1)
    tablero.append(fila_tablero)

# Mostrar el tablero
for fila in tablero:
    print(fila)

# Mostrar tablero
def mostrar_tablero(tablero: list[list[str]]):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()
    print()
# Buscar una pieza y devolver su posición (primera que encuentre)
def buscar_pieza(tablero: list[list[str]], pieza: str):
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == pieza:
                return (i, j)
    return (-1, -1)

# Movimientos de torre
def movimientos_torre(tablero, fila, col):
    moves = []
    # Horizontal
    for c in range(8):
        if c != col:
            moves.append((fila, c))
    # Vertical
    for f in range(8):
        if f != fila:
            moves.append((f, col))
    return moves

# Movimientos de alfil
def movimientos_alfil(tablero, fila, col):
    moves = []
    direcciones = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for df, dc in direcciones:
        f, c = fila + df, col + dc
        while 0 <= f < 8 and 0 <= c < 8:
            moves.append((f,c))
            if tablero[f][c] != ".":
                break
            f += df
            c += dc
    return moves

# Movimientos de reina (torre + alfil)
def movimientos_reina(tablero, fila, col):
    return movimientos_torre(tablero, fila, col) + movimientos_alfil(tablero, fila, col)

# Movimientos de caballo
def movimientos_caballo(tablero, fila, col):
    moves = []
    pasos = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
    for df, dc in pasos:
        f, c = fila + df, col + dc
        if 0 <= f < 8 and 0 <= c < 8:
            moves.append((f,c))
    return moves

# Movimientos de rey
def movimientos_rey(tablero: list[list[str]]) -> list[tuple[int, int]]:
    rey_fila = -1
    rey_col = -1

    # Buscar al rey
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    movimientos = []

    # Posibles desplazamientos del rey
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if df != 0 or dc != 0:
                f = rey_fila + df
                c = rey_col + dc

                if 0 <= f < 8 and 0 <= c < 8:
                    if tablero[f][c] == ".":
                        movimientos.append((f, c))

    return movimientos


# Movimientos de peón (solo hacia adelante, sin capturas)
def movimientos_peon(tablero, fila, col, color="blanco"):
    moves = []
    if color == "blanco":
        if fila > 0 and tablero[fila-1][col] == ".":
            moves.append((fila-1, col))
    else:
        if fila < 7 and tablero[fila+1][col] == ".":
            moves.append((fila+1, col))
    return moves

# Comprobar si un rey está en jaque
def rey_en_jaque(tablero, color="blanco") -> bool:
    rey = "R" if color=="blanco" else "r"
    rey_fila, rey_col = buscar_pieza(tablero, rey)
    if rey_fila == -1:
        return False

    # Revisar alfiles y reinas (diagonal)
    for i in range(8):
        for j in range(8):
            if tablero[i][j] in ("A","Q"):
                if (rey_fila, rey_col) in movimientos_alfil(tablero, i, j):
                    return True
    # Revisar torres y reinas (horizontal/vertical)
    for i in range(8):
        for j in range(8):
            if tablero[i][j] in ("T","Q"):
                if (rey_fila, rey_col) in movimientos_torre(tablero, i, j):
                    return True
    # Revisar caballos
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "C":
                if (rey_fila, rey_col) in movimientos_caballo(tablero, i, j):
                    return True
    # Revisar peones
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "P":
                if (i-1, j-1) == (rey_fila, rey_col) or (i-1, j+1) == (rey_fila, rey_col):
                    return True
    return False

# =======================
# EJEMPLO DE USO
# =======================

tablero = generar_tablero()
tablero[3][3] = "T"   # Torre
tablero[2][2] = "A"   # Alfil
tablero[1][1] = "Q"   # Reina
tablero[5][5] = "C"   # Caballo
tablero[6][3] = "P"   # Peón
tablero[3][4] = "R"   # Rey

print("Tablero inicial:")
mostrar_tablero(tablero)

print("Movimientos torre desde (3,3):", movimientos_torre(tablero, 3, 3))
print("Movimientos alfil desde (2,2):", movimientos_alfil(tablero, 2, 2))
print("Movimientos reina desde (1,1):", movimientos_reina(tablero, 1,1))
print("Movimientos caballo desde (5,5):", movimientos_caballo(tablero, 5,5))
print("Movimientos rey desde (3,4):", movimientos_rey(tablero, 3,4))
print("Movimientos peón desde (6,3):", movimientos_peon(tablero, 6,3))

if rey_en_jaque(tablero):
    print("El rey está en jaque!")
else:
    print("El rey está seguro")


#POSIBLES MOV TORRE
def posibles_movimientos_torre(tablero: list[list[str]], fila: int, columna: int) -> list[tuple[int, int]]:
    movimientos = []
    n = len(tablero)
    
    # Direcciones: arriba, abajo, izquierda, derecha
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for df, dc in direcciones:
        f, c = fila + df, columna + dc
        while 0 <= f < n and 0 <= c < n:
            if tablero[f][c] == "X":
                break  # se encuentra una pieza, se detiene
            movimientos.append((f, c))
            f += df
            c += dc
            
    return movimientos


#TORRE ATACA REY
def torre_ataca_rey(tablero: list[list[str]]) -> bool:
    # 1. Buscar al rey
    rey_fila = -1
    rey_col = -1

    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    # 2. Buscar torres
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "T":

                # Misma fila
                if i == rey_fila:
                    inicio = min(j, rey_col) + 1
                    fin = max(j, rey_col)
                    bloqueado = False

                    for c in range(inicio, fin):
                        if tablero[i][c] != ".":
                            bloqueado = True

                    if not bloqueado:
                        return True

                # Misma columna
                if j == rey_col:
                    inicio = min(i, rey_fila) + 1
                    fin = max(i, rey_fila)
                    bloqueado = False

                    for f in range(inicio, fin):
                        if tablero[f][j] != ".":
                            bloqueado = True

                    if not bloqueado:
                        return True

    return False

#ALFIL ATACA REY 
def alfil_ataca_rey(tablero: list[list[str]]) -> bool:
    # 1. Buscar al rey
    rey_fila = -1
    rey_col = -1

    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    # 2. Direcciones diagonales
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 3. Buscar alfiles
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

#CABALLO ATACA REY

def caballo_ataca_rey(tablero: list[list[str]]) -> bool:
    # 1. Buscar al rey
    rey_fila = -1
    rey_col = -1

    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    # 2. Movimientos del caballo
    movimientos = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    # 3. Buscar caballos
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "C":
                for df, dc in movimientos:
                    f = i + df
                    c = j + dc
                    if f == rey_fila and c == rey_col:
                        return True

    return False

#PEON ATACA REY

def peon_ataca_rey(tablero: list[list[str]]) -> bool:
    # 1. Buscar al rey
    rey_fila = -1
    rey_col = -1

    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    # 2. Buscar peones
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "P":
                # Diagonal izquierda
                if i - 1 == rey_fila and j - 1 == rey_col:
                    return True
                # Diagonal derecha
                if i - 1 == rey_fila and j + 1 == rey_col:
                    return True

    return False


#MOV REY
def movimientos_rey(tablero: list[list[str]]) -> list[tuple[int, int]]:
    rey_fila = -1
    rey_col = -1

    # Buscar al rey
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "R":
                rey_fila = i
                rey_col = j

    movimientos = []

    # Posibles desplazamientos del rey
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if df == 0 and dc == 0:
                continue

            f = rey_fila + df
            c = rey_col + dc

            if 0 <= f < 8 and 0 <= c < 8:
                if tablero[f][c] == ".":
                    movimientos.append((f, c))

    return movimientos
