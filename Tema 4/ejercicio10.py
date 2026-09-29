from Libro import Libro

libros = [
    Libro("Crimen y catigo", "Fiódor Dostoievski", 671, ["Novela", "Filosofía", "Psicología"], 10),
    Libro("Gurra y paz", "León Tolstói", 1225, ["Novela", "Histórica"],10),
    Libro("Anna Karénina", "León Tolstói", 864, ["Novela", "Drama", "Romance"], 9),
    Libro("El maestro y Margarita", "Mijaíl Bulgákov", 384, ["Fantasía", "Satírica"],9),
    Libro("Los hermanos Karamázonv", "Fiódor Dostoievski", 1013, ["Novela", "Filosofía", "Drama"],10),
    Libro(1984, "George Orwell", 328, ["Distopía", "Ciencia ficción"], 10),
    Libro("Cien años de soledad", "Gabriel García Márquez", 471, ["Realismo mágico", "Drama"], 10),
    Libro("Ulises", "James Joyce", 730, ["Experimental", "Filosofía"],8),
    Libro("Moby-Dick", "Herman Melville", 635, ["Aventura", "Clásico"], 9),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, ["Aventura", "Clásico", "Sátira"], 10)
    
]
print(f"Apartado a): ")

[print(libro.nombre) for libro in libros if libro.paginas > 1000 and libro.autores == "Fiódor Dostoievski"]
print(f"Apartado b): ")

[print(libro.nombre) for libro in libros if libro.paginas < 400]

print(f"Apartado c): ")
[print(libro.nombre) for libro in libros if str(libro.nombre) != libro.nombre]

autores = list(set(libro.autores for libro in libros))
print(f"Apartado d): {autores}")       


               