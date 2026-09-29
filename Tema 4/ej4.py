from datetime import datetime
from Jugador import Jugador

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
#MetaAlgoritmo, espero que para examen si hay q ordenar
#Cuando hay que sacar un maximo complejo, Jo no cae
def elegir_capitan(jugadores: list) -> Jugador:
   capitan = jugadores[0]
   for j in jugadores[1:]:
      capitan = masCapitan(capitan,j)
   return capitan

def masCapitan(j1: Jugador, j2: Jugador) -> Jugador:
   if j1.pos_capitan == j2.pos_capitan:
      return j1 if j1.fecha_nacimiento < j2.fecha_nacimiento else j2
   
   if j1.pos_capitan == 0:
      return j2
   
   if j2.pos_capitan == 0:
      return j1
   
   return j1 if j1.pos_capitan < j2.pos_capitan else j2
print(elegir_capitan(atletico_madrid))