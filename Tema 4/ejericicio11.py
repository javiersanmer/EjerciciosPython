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
libroEsp = [
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, ["Aventura", "Clásico", "Sátira"],10),
    Libro("La Regenta", "Leopoldo Alas" "Clarín", 928, ["Novela", "Realismo", "Drama"], 9),
    Libro("Fortunata y Jacinta", "Benito Pérez Galdós", 1056, ["Novela", "Costumbrismo", "Drama"], 9),
    Libro("Campos de Castilla", "Antonio Machado", 208, ["Poesía", "Reflexión"], 9),
    Libro("Platero y yo", "Juan Ramón Jiménez", 138, ["Narrativa", "Poesía en prosa"], 8),
    Libro("Bodas de sangre", "Federico García Lorca", 128, ["Teatro", "Tragedia", "Poesía"], 9),
    Libro("La colmena", "Camilo José Cela", 304, ["Novela", "Costumbrismo"], 8),
    Libro("Nada", "Carmen Laforet", 288, ["Novela", "Existencialismo"], 9),
    Libro("El camino", "Miguel Delibes", 176, ["Novela","Realismo"], 8),
    Libro("Los santos inocentes", "Miguel Delibes", 254, ["Novela", "Drama social"], 9)
]


librosM = set(libro.nombre for libro in libros)
libroEsp = set(libro.nombre for libro in libroEsp)

print(list(libroEsp & librosM))

print(list(libroEsp - librosM))

libroSinRep = []
for libro in libros:
    titulo = str(libro.nombre)
    if titulo[0] == "D":
        repetido = False
        for l in libroSinRep:
            if str(l.nombre) == titulo:
                repetido = True
                break
        if not repetido:
            libroSinRep.append(libro)
for libro in libroSinRep:
    print(libro.nombre)

mejorEsp = max(libroEsp, key=lambda a: list(libroEsp).count(a))

print(f"El mejor autor esp es {mejorEsp}")


libroEsp = [a.nombre for a in libroEsp]
mejorEsp = max(libroEsp, key=libroEsp.count)
print(f"El mejor autor esp es {mejorEsp}")



mejorEsp = max(libroEsp, key=lambda libro: sum(1 for l in libroEsp if l.autor == libro.autor)).autor
print(f"El mejor autor esp es {mejorEsp}")
