import json
from pathlib import Path


class Portatiles:

    def __init__(self, id: int, marca: str, modelo: str, precio: list[str], especificaciones: list[str], valoraciones: list[dict[str]]):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.especificaciones = self.especificaciones
        self.valoraciones = self.valoraciones

    def __str__(self):
        return f"{self.id} - Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio} - Especificaciones: {self.especificaciones} - Valoraciones: {self.valoraciones["usuario"]}, puntuación: {self.valoraciones["puntuacion"]}, comentario: {self.valoraciones["comentario"]}"

if __name__ == "__main__":
    ruta = Path(__file__).parent / "portatiles.json"

    portatiles = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
       
        for p in datos:
            portatiles_datos = Portatiles(
                p["id"],
                p["marca"],
                p["modelo"],
                p["precio"],
                p["especificaciones"],
                p["valoraciones"]
            )
            portatiles.append(portatiles_datos)

    for p in portatiles:
        print(p)