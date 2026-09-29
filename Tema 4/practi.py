from Videojuego import Videojuego

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

[print(j.nombre) for j in juegos if j.puntuacion >= 9 and j.peso < 50]
print("-----------------------------")

ej3 =[print(f"{j.nombre}, precio: {j.precio_final(0.21,0)} ")for j in juegos]
print("-----------------------------")

for j in juegos:
    if j.generos == "RPG":
        desc = 0.25
    else: 
        desc = 0
[print(f"{j.nombre}, {j.precio_final(0.21, desc)}") for j in juegos]

mejores_ps4 = [
   Videojuego("The Last of Us Part II", ["Acción", "Aventura"], "2020-06-19", 9.7, 18, 59.99, 80),
   Videojuego("God of War", ["Acción", "Aventura"], "2018-04-20", 9.6, 18, 49.99, 45),
   Videojuego("Persona 5 Royal", ["RPG", "JRPG"], "2020-03-31", 9.8, 16, 59.99, 30),
   Videojuego("Elden Ring", ["RPG", "Acción", "Souls-like"], "2022-02-25", 9.8, 16, 59.99, 60),
   Videojuego("Horizon Zero Dawn", ["Acción", "Aventura", "Mundo Abierto"], "2017-02-28", 9.3, 16, 39.99, 50)
]


mejores_xbox_x = [
   Videojuego("Halo Infinite", ["FPS", "Acción"], "2021-12-08", 9.0, 16, 59.99, 80),
   Videojuego("Forza Horizon 5", ["Carreras", "Mundo Abierto"], "2021-11-09", 9.5, 3, 59.99, 110),
   Videojuego("Elden Ring", ["RPG", "Acción", "Souls-like"], "2022-02-25", 9.8, 16, 59.99, 60),
   Videojuego("Microsoft Flight Simulator", ["Simulación", "Aviación"], "2020-08-18", 9.0, 3, 59.99, 150),
   Videojuego("Gears 5", ["TPS", "Acción"], "2019-09-10", 8.8, 18, 39.99, 70)
]

mejores_ps4_set = set(j.nombre for j in mejores_ps4)
mejores_xbox_x_set = set(j.nombre for j in mejores_xbox_x)

apartadoA = list(mejores_ps4_set & mejores_xbox_x_set)
print(apartadoA)
apartadoB = list(mejores_ps4_set - mejores_xbox_x_set)
print(apartadoB)
apartadoC = list(mejores_xbox_x_set - mejores_ps4_set)
print(apartadoC)

from Planeta import Planeta
from datetime import datetime

planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna",1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4,1.60659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Júpiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.4819e23], ["Calisto", 2.410e6, 1.0759e23], ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titán", 2.575e6, 1.345e23], ["Rea", 1.527e6, 2.3166e21], ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, datetime.min, [["Caronte", 6.057e5, 1.586e21]])
]

[print(f"{p.nombre}, densidad: {p.get_densidad()}") for p in planetas]

mayorDensidad = max(planetas, key=lambda p:p.get_densidad())
print(mayorDensidad.nombre)

for p in planetas:
    for luna in planetas.lunas:
        if luna[0] == "Luna":
            radioLuna = luna[1]
            break
lunasGrandes = []
for p in planetas:
    for luna in planetas.lunas:
        if luna[1] > radioLuna:
            lunasGrandes.append(luna[0])

lunasRadios = [r for r in planetas.lunas[1]]
lunaPeque = [min(lunasRadios, key=lambda p:p.nombre)]
print(lunaPeque)