from Videojuego import Videojuego

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

juegosPs4 = set(juego.nombre for juego in mejores_ps4)
juegosXbox = set(juego.nombre for juego in mejores_xbox_x)

print(list(juegosPs4 & juegosXbox ))
print(list(juegosPs4 - juegosXbox))
print(list(juegosXbox - juegosPs4))


