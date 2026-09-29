numSecreto = 22
haAcertado = False
contador = 0

while not haAcertado:
    numero = int(input("Introduce un número: "))
    contador = contador + 1

    if numero == numSecreto:
        print(f"Has acertado. Te ha tomado {contador} intentos")
    elif numero > numSecreto:
        print("El numero es menor")
    elif numero < numSecreto:
        print("El numero es  mayor")