import random
def mostrarHuecos(palabra: str, letraAcierto: list[str]):
    huecos = []
    for letra in palabra:
        if letra in letraAcierto:
            huecos.append(letra)
        else:
            huecos.append("_")
    print(huecos)

def pideLetra() -> str:
    letraInicial = input("Introduce una letra: ")
    letra = letraInicial.upper()
    return letra

def menuJuego(vidas: int, palabra:str, letraAcierto: list[str]):
    print(f"Tienes {vidas} vidas")
    print("Palabra que debes encontrar: ")
    mostrarHuecos(palabra, letraAcierto)
 
def eligePalabra(nNivel:int) -> str:
    nivel1 = ("TAZA", "GATO", "LORO", "MESA")
    nivel2 = ("PARTIR", "ESPERA", "SUFRIR", "PYTHON" )       
    nivel3 = ("PELICULA", "CANGREJO", "SOMBRERO", "TORNILLO")
    
    if nNivel == 1:
        listaNivel = nivel1
    elif nNivel == 2:
        listaNivel = nivel2
    elif nNivel == 3:
        listaNivel = nivel3

    return listaNivel[random.randint(0, len(listaNivel) - 1)]

def vidasTotales(letrasAcierto: list[str],palabra:str, letra:str, vidas:int) -> int:
    if letra in letrasAcierto:
        print("Ya has probado")
        vidas -=1
    else:
        encontrado = False
        for i in palabra:
            if i == letra:
                encontrado = True
                break
        if encontrado:
            print("Has encontrado una letra! Te sumo una vida")
            letrasAcierto.append(letra)
            vidas += 1
        else:
            print("Has fallado :(, pierdes una vida")
            vidas -= 1
    return vidas

def palabraCompletada(palabra: str, letraAcierto: list[str]) -> bool:
    completada = True
    for p in palabra:
        if p not in letraAcierto:
            completada = False
    return completada

def jugar(palabra: str, vidas: int) -> int:
    letrasAcierto = []
    
    while vidas > 0:
        menuJuego(vidas, palabra, letrasAcierto)
        letra = pideLetra()
        vidas = vidasTotales(letrasAcierto,palabra, letra, vidas)

        if palabraCompletada(palabra, letrasAcierto):
            print("Enhorabuena has encontrado la palabra: ")
            for p in palabra:
                print(p, end= " ")
            break
    if vidas == 0:
        print("Has perdido, la palabra era: ")
        for p in palabra:
            print(p, end= " ")
    return vidas