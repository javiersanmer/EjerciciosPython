from tresenraya import imprimirtablero, insertarJugada, ia, estado

tablero = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
imprimirtablero(tablero)
turno = 0

while True:
    insertarJugada(tablero)
    imprimirtablero(tablero)
    estadoPartida = estado(tablero)
    if estado(tablero) == 1:
        print("Has ganado")
        break

    if turno == 5:
        print("EMPATE")
        break
    
    input("La IA juega: ")
    ia(tablero)
   
    estadoPartida = estado(tablero)
    imprimirtablero(tablero)

    if estadoPartida == -1:
        print("Has perdido")
        break
    ia(tablero)
     
    turno += 1
