import random

def caraCruz(nVeces : int) -> str:
    i = 0
    for i in range(nVeces):
        num = random.randint(0,1)
        if num == 0:
            print("Cruz")
        else:
            print("Cara")

nVeces = int(input("Elige las monedas que quieres lanzar: "))
caraCruz(nVeces)