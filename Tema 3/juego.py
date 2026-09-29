import funciones
vidas = 10
nNivel = 1
maxNivel = 3

while nNivel <= maxNivel and vidas > 0:
    print("-------------------")
    print(f"Nivel {nNivel}")
    print("-------------------")

    palabra =  funciones.eligePalabra(nNivel)
    vidas = funciones.jugar(palabra, vidas)
    
    if vidas <= 0:
        break

    if nNivel == maxNivel:
        print("HAS GANADO")
        break
    else:
        print(f"Subes al nivel {nNivel + 1}")
        nNivel += 1


