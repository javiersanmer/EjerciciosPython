import random

def generar_partitura(longitud: int, nRepeticiones:int) -> list[str]:
    notas = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    partitura = []
    iguales = None
    for _ in range(longitud):
        if len(partitura)  < nRepeticiones:
            partitura.append(notas[random.randint(0, len(notas)-1)])
        else:
            ultimas = partitura[-nRepeticiones:]
            iguales = True
            for n in ultimas:
                if n != ultimas[0]:
                    iguales = False
                    break
        
        if iguales:
            opciones = []
            for nota in notas:
                if nota != partitura[-1]:
                    opciones.append(nota)
            partitura.append(opciones[random.randint(0, len(opciones)-1)])
        else:
            partitura.append(notas[random.randint(0, len(notas) - 1)])
    return partitura

print(generar_partitura(20,2))
