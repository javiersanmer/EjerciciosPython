from datetime import datetime
from Jugador import Jugador
from datosJug import get_datos

atletico_madrid = get_datos()

def f2a(jugadores: list[Jugador]) -> Jugador:
    jugadoMasPartidos = max(jugadores, key = lambda jugador:jugador.partidos_jugados)
    return jugadoMasPartidos.nombre

def f2b(jugadores: list[Jugador]) -> Jugador:
    jugadorMejorRatio = max(jugadores, key=lambda jugador:jugador.ratio_goles())
    return jugadorMejorRatio.nombre

def f2c(jugadores: list[Jugador]) -> Jugador:
    defensaMasGoles = max(jugadores, key=lambda jugador:jugador.goles)
    return defensaMasGoles.nombre
def f2d(jugadores:list[Jugador]) -> list[Jugador]:
    denfensa = max([j for j in jugadores if j.posicion == "Defensa"], key = lambda j: j.ratio_goles())
    centro = max([j for j in jugadores if j.posicion == "Centrocampista"], key = lambda j: j.ratio_goles())
    delanteroGoles = max([j for j in jugadores if j.posicion == "Delantero"], key = lambda j: j.ratio_goles())
    return [denfensa, centro, delanteroGoles]

def tiempo_pasado(nacimiento: datetime) -> int:
   hoy = datetime.now()
   # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
   edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
   return edad

def f2e(jugadores:list[Jugador]) -> list[Jugador]:
    return [j.nombre for j in jugadores if tiempo_pasado(j.fecha_nacimiento) <= 28]

def f2f(jugadores: list[Jugador]) -> list[Jugador]:
    return [j.nombre for j in jugadores if j.goles == 0 and j.posicion != "Portero"]

def f2g(jugadores: list[Jugador]) -> list[Jugador]:
    return [j.nombre for j in jugadores if j.fecha_alta.year < 2015]

def f2h(jugadores: list[Jugador]) -> list[Jugador]:
    menosDelantero = min(jugador.goles for jugador in jugadores if jugador.posicion == "Delantero")
    return [j.nombre for j in jugadores if j.posicion == "Centrocampista" and j.goles > menosDelantero]

def f2i(jugadores: list[Jugador]) -> dict[str, int]:
    posiciones = ["Portero", "Defensa","Delantero","Centrocampista"]
    resultado = {}

    for p in posiciones:
        resultado[p] = sum(j.goles for j in jugadores if j.posicion == p)
    return resultado

def f2j(jugadores: list[Jugador]) -> dict[str, int]:
    posiciones =  ["Portero", "Defensa","Delantero","Centrocampista"]
    resultado = {}

    for p in posiciones:
        resultado[p] = [j.nombre for j in jugadores if j.posicion == p]
    return resultado

def f2k(jugadores: list[Jugador]) -> dict[str, list[Jugador]]:
    claves = ["Debutante", "Principiante", "Senior", "Veterano"]
    resultado = {}

    for c in claves:
        if c == "Veterano":
            resultado[c] = [j for j in jugadores if j.fecha_alta.year == 2022]
        elif c == "Senior":
            resultado[c] = [j for j in jugadores if j.fecha_alta.year > 2020 and j.fecha_alta.year < 2022]
        elif c == "Principiante":
            resultado[c] = [j for j in jugadores if  j.fecha_alta.year > 2015 and j.fecha_alta.year < 2020]
        else:
            resultado[c] = [j for j in jugadores if j.fecha_alta.year < 2015]

    return resultado
              
print(f2a(atletico_madrid))
print(f2b(atletico_madrid))
print(f2c(atletico_madrid))
print(f2d(atletico_madrid)[0].nombre)
print(f2d(atletico_madrid)[1].nombre)
print(f2d(atletico_madrid)[2].nombre)
print(f2e(atletico_madrid))
print(f2f(atletico_madrid))
print(f2g(atletico_madrid))
print(f2h(atletico_madrid))
print("--------------------------------")

resultado1 = f2i(atletico_madrid)

for posicion, goles in resultado1.items():
    print(f"{posicion}: {goles} goles")

print("--------------------------------")

resultado2 = f2j(atletico_madrid)

for posicion, goles in resultado2.items():
    print(f"{posicion}: {goles} goles")



print("--------------------------------")
resultado3 = f2k(atletico_madrid)

for claves, anio in resultado3.items():
    nombres = [j.nombre for j in atletico_madrid]
    print(f"{claves}: {nombres}")
     
    
seleccion_espanola = [
   Jugador("Unai Simón", 23, "Portero", 40, 0, 1, 5, 0, datetime(1997, 6, 11), datetime(2020, 9, 1), True),
   Jugador("Dani Carvajal", 2, "Defensa", 80, 2, 1, 15, 1, datetime(1992, 1, 11), datetime(2014, 9, 4), True),
   Jugador("Aymeric Laporte", 14, "Defensa", 35, 3, 0, 5, 0, datetime(1994, 5, 27), datetime(2021, 5, 11), True),
   Jugador("Pau Torres", 4, "Defensa", 30, 2, 0, 3, 0, datetime(1997, 1, 16), datetime(2019, 11, 15), True),
   Jugador("Jordi Alba", 18, "Defensa", 90, 10, 1, 20, 2, datetime(1989, 3, 21), datetime(2012, 7, 5), True),
   Jugador("Carlos Soler", 19, "Centrocampista", 18, 3, 0, 2, 0, datetime(1997, 1, 2), datetime(2021, 9, 2), True),
   Jugador("Pedri", 16, "Centrocampista", 25, 5, 0, 2, 0, datetime(2002, 11, 25), datetime(2020, 9, 25), True),
   Jugador("Gavi", 9, "Centrocampista", 20, 4, 0, 3, 0, datetime(2004, 8, 5), datetime(2021, 10, 6), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 120, 1, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True),
   Jugador("Ferran Torres", 11, "Delantero", 45, 15, 0, 5, 0, datetime(2000, 2, 29), datetime(2020, 9, 3), True),
   Jugador("David Raya", 13, "Portero", 5, 0, 0, 1, 0, datetime(1995, 9, 15), datetime(2022, 3, 15), False),
   Jugador("Íñigo Martínez", 3, "Defensa", 35, 2, 0, 4, 0, datetime(1991, 5, 17), datetime(2013, 8, 14), False),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), False),
   Jugador("Borja Iglesias", 22, "Delantero", 10, 5, 0, 1, 0, datetime(1993, 1, 17), datetime(2022, 9, 24), False)
]

print("-------------------------")
jugadoresAM = set(j.nombre for j in atletico_madrid)
jugadoresESP = set(j.nombre for j in seleccion_espanola)


apartadoA = list(jugadoresAM & jugadoresESP)
[print(jugador) for jugador in apartadoA]


print("-------------------------")
jugadoresAMTitular = set(j.nombre for j in atletico_madrid if j.titular)
jugadoresESPTitular = set(j.nombre for j in seleccion_espanola  if j.titular)


apartadoB = list(jugadoresESPTitular & jugadoresAMTitular)
[print(jugador) for jugador in apartadoB]

def elegir_capitan(jugadores: list)->Jugador:
    for j in jugadores:
        if j.titular:
            print(j)
    return j

























