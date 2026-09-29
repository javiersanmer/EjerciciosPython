import json
from pathlib import Path


class Producto:

    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.id} - Nombre: {self.nombre} - Precio: {self.precio} - Stock: {self.stock}"
    
if __name__ == "__main__":

    ruta = Path(__file__).parent / "productos.json"

    productos = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f) #devuelve una lista de diccionarios sis empieaz por llave, pero si es por corchete deevuelve una lista de dicionarios o algo asi arreglar

        for d in datos: #d es un diccionario
            prod = Producto(
                d["id"],
                d["nombre"],
                d["precio"],
                d["stock"]
            )
            productos.append(prod)
    for p in productos:
        print(p)