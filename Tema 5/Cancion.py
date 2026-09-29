from datetime import datetime

class Cancion:
    def __init__(self, id: int,titulo: str, artistas: list[str], album: str, generos: list[str], duracion: int, fecha_salida: datetime) -> None:
        self.id = id
        self.titulo = titulo
        self.artitas = artistas
        self.album = album
        self.generos = generos 
        self.duracion = duracion
        self.fecha_salida = fecha_salida
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Cancion):
            return self.id == other.id
        return False

    def __lt__(self, other) -> bool:
        return self.duracion < other.duracion
    
    def __le__(self, other) -> bool:
        return self.duracion <= other.duracion

    def __gt__(self, other) -> bool:
        return self.duracion > other.duracion

    def __ge__(self, other) -> bool:
        return self.duracion >= other.duracion

    def año(self) -> int:
        return self.fecha_salida.year
    
    def __str__(self) -> str:
        str_artistas = ", ".join(self.artistas)
        str_artistas +=  f" y {self.artistas[-1]}"
        return f"{self.titulo} -- {str_artistas}" 
    