import random
def emparejar(n1: list[str] , n2:list[str]):

    emparejamiento = len(n1)
    for _ in range(emparejamiento):
        equipos1 = n1[random.randint(0, len(n1) - 1)]
        equipos2 = n2[random.randint(0, len(n2) - 1)]
        n1.remove(equipos1)
        n2.remove(equipos2)
        print(f"{equipos1} vs {equipos2}")

equipos1 = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Bilbao"]
equipos2 = ["Real Sociedad", "Betis", "Granada", "Valencia"]

print("#### PARTIDOS: ####")
emparejar(equipos1.copy(), equipos2.copy())