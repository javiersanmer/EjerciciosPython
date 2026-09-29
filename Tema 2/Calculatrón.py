vidasIniciales = 3
dificultad = 1

opcionMenu = 0

while opcionMenu == 0:
    vidas = vidasIniciales
    cuenta = 0
	
    print("Bienvenido/a a Calculatrón, elige una opción: ") 
    print("1.Jugar") 
    print("2.Configurar")
    print("0.Salir") 

    opcionMenu = int(input("Introduce una opción del menú: "))

    if opcionMenu == 1:
        if dificultad == 1:
            while(vidas == 0):
                num1 = 10
                num2 = 10
                simb = 2

                if simb == 0:
                    print(f"Resuelve {num1 + num2}")
                    solucion = int(input())
                    respuesta = num1 + num2
                elif simb == 1:
                    print(f"Resuelve {num1 - num2}")
                    respuesta = num1 + num2
                    solucion = int(input())
                elif simb == 2: 
                    print(f"Resuelve {num1 * num2}")
                    respuesta = num1 + num2
                    solucion = int(input())

            if respuesta != solucion:
                vidas != vidas - 1

                print("Has fallado")
                print(f"El resultado era {respuesta}")
                print(f"Te quedan {vidas}")
            else:
                cuenta = cuenta + 1
            
            print(f"Has acertado un total de {cuenta} cuentas")

        elif dificultad == 2:
            while(vidas != 0):
                num1 = 2
                num2 = 3

                simb = 2
'''
logro con ture  yfalsa
imprimMenuCon
imprimim
6 fuuncion 96 y 126
'''