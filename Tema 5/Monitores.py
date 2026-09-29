from datetime import datetime

class Monitores:
    def __init__(self, codigo : str, nombre : str, pulgadas : float, modelo: list, tactil : bool, fecha_compra : datetime, precio_venta : float):
        self.codigo = codigo
        self.nombre = nombre
        self.pulgadas = pulgadas
        self.modelo = modelo
        self.tactil = tactil
        self.fecha_compra = fecha_compra
        self.precio_venta = precio_venta

    def __str__(self):
        return (
           f"Nombre: {self.nombre}\n"
           f"Código: {self.codigo},\n"
           f"Pulgadas: {self.pulgadas},\n"
           f"Modelo: {self.modelo},\n"
           f"OLED: {self.oled}, "
           f"Fecha_compra: {self.fecha_compra}, "
           f"Precio: {self.precio_venta}"
        )

