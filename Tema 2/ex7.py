import random
def generaCarta() -> str:#como dice devolvera signfica que ahabra un return  
    valorNum = random.randint(1,13)
    valorNum = str(valorNum)
    if valorNum == 11:
        valorNum = "J"
    elif valorNum == 12:
        valorNum = "Q"
    elif valorNum == 13:
        valorNum = "K"

    textoOpc = random.randint(1,4)

    if textoOpc == 1:
        textoPal = "de corazones"
    elif textoOpc == 2:
        textoPal = "de picas"
    elif textoOpc == 3:
        textoPal = "de diamantes"
    elif textoOpc == 4:
        textoPal = "de tréboles"

    carta = f"{valorNum} {textoPal}"
    return carta

contador = 0
cartaEncontrada = 0
primeraParteContador = 0

cartaElegida = input(f"Elige una carta: ")

while cartaEncontrada < 2:
    contador = contador + 1
    cartaSacada = generaCarta()
    print(f"Tirada {contador}: {cartaSacada}")

    if cartaElegida == cartaSacada:
        cartaEncontrada = cartaEncontrada + 1
        if primeraParteContador == 0:
            primeraParteContador = contador

print(f"La primera vez que se sacó la carta {cartaElegida} fue en la 'tirada' {primeraParteContador}")
