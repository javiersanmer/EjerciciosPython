import random
puntosHumano = 0 
puntosBot = 0
ronda = 1

while True:
    if puntosHumano == 3:
        print("Has ganado al bot")
        break
    elif puntosBot == 3:
        print("Has perdido")
        break
        
    print(f"Ronda: {ronda}")
    eligeHumano = input("Elige piedra, papel o tijera: ")

    eligeBot = random.randint(0,2)
    
    if eligeBot == 0:
        eligeBotJugada = "Piedra"
    elif eligeBot == 1:
        eligeBotJugada = "Papel"
    else:
        eligeBotJugada = "Tijera"
    
    print(f"El bot ha usado: {eligeBotJugada}")

    if eligeHumano == "Piedra":
        if eligeBotJugada == "Piedra":
            resultado = 0
        elif eligeBotJugada == "Tijera":
            resultado = 1
        else:
            resultado = -1
    elif eligeHumano == "Papel": 
        if eligeBotJugada == "Piedra":
            resultado = 1
        elif eligeBotJugada == "Tijera":
            resultado = -1
        else:
            resultado = 0
    elif eligeHumano == "Tijera":
        if eligeBotJugada == "Piedra":
            resultado = -1
        elif eligeBotJugada == "Tijera":
            resultado = 0
        else:
            resultado = 1

    if resultado == -1:
        print("Has perdido")
        puntosBot = puntosBot +1
    elif resultado == 0:
        print("Empate")
    else:
        print("Has ganado")
        puntosHumano = puntosHumano +1

    ronda = ronda +1

