class Libro:
    def __init__(self, nombre: str, autores: list, paginas: int, generos: list, puntuacion: int):
        """
        Constructor de la clase Libro.
        
        :param nombre: Nombre del libro.
        :param autores: Lista de autores.
        :param paginas: Número de páginas.
        :param generos: Lista de géneros literarios.
        :param puntuacion: Puntuación del libro (de 0 a 10).
        """
        self.nombre = nombre
        self.autores = autores
        self.paginas = paginas
        self.generos = generos
        self.puntuacion = max(0, min(puntuacion, 10))  # Asegura que esté entre 0 y 10

    def __str__(self):
        """Representación en cadena del libro."""
        return (f"📖 {self.nombre}\n"
                f"✍ Autores: {', '.join(self.autores)}\n"
                f"📑 Páginas: {self.paginas}\n"
                f"📚 Géneros: {', '.join(self.generos)}\n"
                f"⭐ Puntuación: {self.puntuacion}/10")

    def es_tocho(self):
        """Determina si el libro es largo (más de 500 páginas)."""
        return self.paginas > 500

    def actualizar_nota(self, cambio: int):
        """Cambia la puntuación del libro sin exceder 10."""
        self.puntuacion = max(0, min(self.puntuacion+cambio, 10))