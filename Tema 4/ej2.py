from datetime import datetime
from Jugador import Jugador

def f2a(jugadores:list) -> Jugador:
    jugadorMasPartidos = max(jugadores, key = lambda jugador: jugador.partidos_jugados)
    return jugadorMasPartidos.nombre

def f2b(jugadores: list) -> Jugador:
    jugadorMejorRatio = max(jugadores, key = lambda jugador : jugador.ratio_goles())
    return jugadorMejorRatio.nombre

def f2c(jugadores: list) -> Jugador:
    defensas = [jugador for jugador in jugadores if jugador.posicion == "Defensa"]
    defensaMasGoles = max(defensas, key = lambda jugador : jugador.goles)
    return defensaMasGoles.nombre

def f2d(jugadores: list) -> list:
    denfensa = max([j for j in jugadores if j.posicion == "Defensa"], key = lambda j: j.goles)
    centrocampista = max([j for j in jugadores if j.posicion == "Centrocampista"], key = lambda j: j.goles)
    delantero =  max([j for j in jugadores if j.posicion == "Delantero"], key = lambda j: j.goles)

    return [denfensa, centrocampista, delantero]

def tiempo_pasado(nacimiento: datetime) -> int:
   hoy = datetime.now()
   # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
   edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
   return edad

def f2e(jugadores: list[Jugador]) -> list:
    return [jugador.nombre for jugador in jugadores if tiempo_pasado(jugador.fecha_nacimiento) <= 28]

def f2f(jugadores: list) -> list:
    return [jugador.nombre for jugador in jugadores if jugador.posicion != "Portero" and jugador.goles == 0]

def f2g(jugadores: list) -> list:
    return [jugador.nombre for jugador in jugadores if jugador.fecha_alta.year <= 2015]

def f2h(jugadores: list) -> list:
    menosGolesDelantero = min(jugador.goles for jugador in jugadores if jugador.posicion == "Delantero")
    return [j.nombre for j in jugadores if j.goles > menosGolesDelantero and j.posicion == "Centrocampista"]

def f2i(jugadores: list[Jugador]) -> dict[str, int]:
    posiciones = ["Portero", "Defensa","Delantero","Centrocampista"]
    resultado = {}

    for p in posiciones:
        resultado[p] = sum(j.goles for j in jugadores if j.posicion == p)
    return resultado

def f2j(jugadores: list[Jugador]) -> dict[str, list[Jugador]]:
    posiciones = ["Portero", "Defensa", "Centrocampista", "Delantero"]
    resultado = {}
    for p in posiciones:
        resultado[p] = [j for j in jugadores if j.posicion == p]
    return resultado

#si pusiesta list[str], entonces si seria j.nombre

#def f2k(jugadores: list[Jugador]) -> dict[str, list[Jugador]]:
    antigueJugador = ["Debutante", "Principiante", "Senior", "Veterano"]
    resultado = {}
    for p in antigueJugador:
        resultado[p] = [j.nombre for j in jugadores if j.fecha_alta < j.fecha_alta.year == 2022]
    for p in antigueJugador:    
        resultado[p] = [j.nombre for j in jugadores if j.fecha_alta < (j.fecha_alta.year == 2022 and j.fecha_alta.year == 2020)]
    for p in antigueJugador: 
        resultado[p] = [j.nombre for j in jugadores if j.fecha_alta < (j.fecha_alta.year == 2015)]
 
atletico_madrid  = [
   Jugador("Jan Oblak", 13, "Portero", 300, 0, 3, 10, 1, datetime(1993, 1, 7), datetime(2014, 7, 16), True),
   Jugador("José María Giménez", 2, "Defensa", 250, 10, 2, 40, 2, datetime(1995, 1, 20), datetime(2013, 4, 1), True),
   Jugador("Stefan Savic", 15, "Defensa", 230, 5, 0, 50, 3, datetime(1991, 1, 8), datetime(2015, 7, 20), True),
   Jugador("Mario Hermoso", 22, "Defensa", 150, 0, 0, 30, 1, datetime(1995, 6, 18), datetime(2019, 7, 18), True),
   Jugador("Nahuel Molina", 16, "Defensa", 50, 3, 0, 10, 0, datetime(1998, 4, 6), datetime(2022, 7, 28), True),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), True),
   Jugador("Marcos Llorente", 14, "Centrocampista", 200, 30, 0, 40, 1, datetime(1995, 1, 30), datetime(2019, 7, 1), True),
   Jugador("Rodrigo De Paul", 5, "Centrocampista", 70, 10, 0, 20, 0, datetime(1994, 5, 24), datetime(2021, 7, 12), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Antoine Griezmann", 7, "Delantero", 450, 180, 5, 40, 2, datetime(1991, 3, 21), datetime(2014, 7, 28), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 110, 4, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True),
   Jugador("Ivo Grbic", 1, "Portero", 20, 0, 0, 1, 0, datetime(1996, 1, 18), datetime(2020, 8, 20), False),
   Jugador("Reinildo Mandava", 1, "Portero", 60, 2, 0, 15, 1, datetime(1994, 1, 21), datetime(2022, 1, 31), False),
   Jugador("Pablo Barrios", 24, "Centrocampista", 15, 0, 0, 5, 0, datetime(2003, 6, 15), datetime(2022, 1, 12), False),
   Jugador("Memphis Depay", 19, "Delantero", 30, 10, 0, 6, 1, datetime(1994, 2, 13), datetime(2023, 1, 20), False)
]
print(f"2a. Jugador con mas partidos {f2a(atletico_madrid)}")
print("--------------")
print(f"2b. Jugador con mejor ratio goleador {f2b(atletico_madrid)}")
print("--------------")
print(f"2c. Defensa con más goles {f2c(atletico_madrid)}")
print("--------------")
masgoleadores = f2d(atletico_madrid)
print(f"2d.Mejor ratio goleador: ")
print(f"\tDefensa:{masgoleadores[0].nombre}")
print(f"\tCentrocampista:{masgoleadores[1].nombre}")
print(f"\tDelantero:{masgoleadores[2].nombre}")
print("--------------")
print(f"2e. Los jugadores con 28 años o menos son: {f2e(atletico_madrid)}")
print("--------------")
print(f"2f. Los jugadores que nunca han metido gol y que no son porteros {f2f(atletico_madrid)}")
print("--------------")
print(f"2g. Los jugadores que llevan el equipo desde antes de 2015 son: {f2g(atletico_madrid)}")
print("--------------")
print(f"2h. Los centrocampistas que han marcado más goes que algún delantero son: {f2h(atletico_madrid)}")
print(f2i(atletico_madrid))
print(f2j(atletico_madrid))
#print(f2k(atletico_madrid))



resultado1 = f2i(atletico_madrid)

for posicion, goles in resultado1.items():
    print(f"{posicion}: {goles} goles")

resultado2 = f2j(atletico_madrid)

for posicion, goles in resultado2.items():
    print(f"{posicion}: {goles} goles")