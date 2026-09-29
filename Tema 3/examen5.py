from random import randint
elementos = [
    ["Hidrógeno", "H"],
    ["Helio", "He"],
    ["Litio", "Li"],
    ["Berilio", "Be"],
    ["Boro", "B"],
    ["Carbono", "C"],
    ["Nitrógeno", "N"],
    ["Oxígeno", "O"],
    ["Flúor", "F"],
    ["Neón", "Ne"]
]

vidas = 3
print("JUEGOS DE SÍMBOLOS QUÍMICOS")

while vidas > 0:
    elementoAleatorio = randint(0,len(elementos)-1)

    for i, elemento in enumerate(elementos):
        if i == elementoAleatorio:

            print(f"Adivina el simbolo del elemento:  {elemento[0]}")
            elementoElegido = input("Tu respuesta: ")
            if elemento[1] == elementoElegido:
                print("Correcto")
            else:
                print("Incorrecto")
                vidas -=1 
            elementos.remove(elemento)
            
    if vidas == 0:
        print("Te has quedado sin vidas. Fin del juego.")

    if len(elementos) == 0:
        print("Has ganado")
        break
#Tienen que ser simiulares ppero lsuficientemente distintios para que no sea copiar y pegar
#Adjedreaaz, movimiento piezas, ejercicio 4. EJercicio dificil 2 puntos
