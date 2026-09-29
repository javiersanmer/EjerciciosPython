from Videojuego import Videojuego
from datetime import datetime

v = Videojuego(
   "Resident Evil",
   ["Terror", "Acción"],
   "5/5/1996",
   9.6,
   18,
   10.99,
   1.45
)


print(v.apto_menores) #muestra casilla ram

#Ordenar videojuegos por nota

juegos = [
    Videojuego("The Witcher 3", ["RPG", "Acción","Aventura"], "2015-05-19",9.7,18,39.99,50),
    Videojuego("Grand Theft Auto 5", ["Acción", "Mundo abierto"], "2013-09-17", 9.5,18,29.99,95),
    Videojuego("The Legend of Zelda: Breath of the Wild", ["Aventura", "Mundo abierto"], "2017-03-03", 10.0, 12, 59.99,13.4),
    Videojuego("Minecraft", ["Supervivencia", "Sandbox"], "2011-11-18", 9.0,7,26.95,1.2),
    Videojuego("Red Dead Redemption 2", ["Acción", "Mundo abierto"], "2018-10-26", 9.8, 18, 59.99, 150),
    Videojuego("God of War(2018)", ["Acción", "Aventura"], "2018-04-20", 9.6,18,49.99,45),
    Videojuego("Animal Crossing: New Horizons", ["Simulación", "Social"], "2020-03-20", 9.1,3,49.99,10.2),
    Videojuego("Cyberpunk 2077", ["RPG", "Mundo Abierto"], "2020-12-10", 8.5,18,59.99,70),
    Videojuego("Super Mario Odyssey", ["Plataformas", "Supervivencia"], "2017-10-27", 9.8,7,49.99,5.6)
]

v2 = sorted(juegos, key=lambda v: v.puntuacion)
for v in v2:
    print(f"{v.nombre}. {v.puntuacion}")
#De mejor puntu a peor
v2 = sorted(juegos, key=lambda v: v.puntuacion, reverse = True)
for v in v2:
    print(f"{v.nombre}. {v.puntuacion}")

#Contenido exámen
#Clase dada,