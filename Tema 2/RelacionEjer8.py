import random
def cartaAzar() -> str:
    numAleatorio = random.randint(1,12)

    if numAleatorio == 10:
        numAleatorio = "Sota"
    elif numAleatorio == 11:
        numAleatorio = "Caballo"
    elif numAleatorio == 12:
        numAleatorio = "Rey"
    else:
        numAleatorio = str(numAleatorio)

    paloAleatorio = random.randint(1,4)

    if paloAleatorio == 1:
        paloGenerado = "de oros"
    elif paloAleatorio == 2:
        paloGenerado = "de copas"
    elif paloAleatorio == 3:
        paloGenerado = "de bastos"
    elif paloAleatorio == 4:
        paloGenerado = "de espadas"
    
    carta = f"{numAleatorio} {paloGenerado}"

    return carta

i = 0

introdCarta = input("Elige una carta: ")

while True:
    cartaAle = cartaAzar()

    print(f"Carta {i}: {cartaAle}")
    

    if cartaAle == introdCarta:
        print(f"Carta encontrada en la carta {i}")
        break
    
    i += 1
