import random
def lanzarMoneda():
    lanzamiento = random.randint(0,1)

    if lanzamiento == 0:
        print("Cara")
    else:
        print("Cruz")

def lanzarMonedas(nMoneda : int):
    for i in range(nMoneda):
        lanzarMoneda()

def lanzarDado():
    dado = random.randint(1,6)
    print(dado)

def lanzarDados(nDados : int):
    for i in range(nDados):
        lanzarDado()