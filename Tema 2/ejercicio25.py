numSecreto = 22
contador = 1
haAcertado = False

while not haAcertado:
    contador = contador + 1
    numeroIntroducido = int(input("Adivina el numero: "))

    if numeroIntroducido == numSecreto:
        print(f"Has adivinado el número secreto, te ha tomado {contador} intentos")
    elif numeroIntroducido < numSecreto:
        print("No es correcto, es mayor")
    elif numeroIntroducido > numSecreto:
        print("No es correcto, es menor")


