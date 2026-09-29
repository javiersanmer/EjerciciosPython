from datetime import datetime
from random import shuffle
from Cancion import Cancion

class Playlist:
    def __init__(self, id: int, nombre: str, canciones: list[Cancion]) -> None:
        self.id = id
        self.nombre = nombre
        self.canciones = canciones
    
    def __str__(self):
        return(
            f"Identificador Playlist: {self.id}"
            f"Nombre: {self.nombre}"
            f"Canciones: {self.canciones}"
        )
    
    def aniadir_cancion(self, cancion: Cancion) -> None:
        self.cancion.append(cancion)
    
    def eliminar_cancion(self, cancion: Cancion) -> bool:
        for cancion in self.canciones:
            if cancion.id == cancion:
                self.canciones.remove(cancion)
                return True
        return False
    
    def duracion_total(self, cancion: Cancion) -> float:
        return sum(self.canciones)
    
    def buscar_por_artista(self, artista: str) -> list[Cancion]:
        resultado = []
        for nombre in self.nombre:
            if artista in nombre.artistas:
                resultado.append(nombre)
        return resultado
    
    def buscar_por_genero(self, genero: str) -> list[Cancion]:
        resultado = []
        for nombre in self.nombre:
            if genero in nombre.generos:
                resultado.append(nombre)
        return resultado

    def año(self) -> Cancion:
        return self.canciones
    
    def cancion_mas_corta(self) -> Cancion | None:
        if len(self.canciones) == 0:
            return None
        return min(self.canciones)
    
    def cancion_mas_larga(self) -> Cancion | None:
        if len(self.canciones) == 0:
            return None
        return max(self.canciones)
    
    def ordenar_por_duracion(self) -> list[Cancion]:
        return sorted(self.canciones)
    
    def aleatorio(self):
        resultado = sorted(shuffle(self.canciones))
        return resultado


if __name__ == '__main__':
    c1 = Cancion("1","jose","pegao","dance hall","300", datetime(2025,2,1))
    c2 = Cancion("2","jose","pegao2","dance hall2.0","301", datetime(2025,2,1))
    pl = Playlist(
        id = 12,
        nombre="Playlist de novea",
        canciones=[c1,c2]
    )
    cancion = pl.cancion_mas_corta()
    print(cancion if cancion else "No hay canciones")

    print(pl.duracion_total(c1))