from datetime import datetime
from Periodico import Periodico

class Papel(Periodico): 
    INCLUYE_FASCICULOS = 0.50

    def __init__(self, nombre:str, titular:str, autor: str, fecha_salida:datetime, num_edicion:int, calidad_impresion:str, cantidad:int, precio:float, fasciculos:bool, vendidos:int) -> None:
        super().__init__(nombre, titular, autor, fecha_salida)
        self.num_edicion = num_edicion
        self.calidad_impresion = calidad_impresion
        self.cantidad = cantidad
        self.precio = precio
        self.fasciculos = fasciculos 
        self.vendidos = vendidos

    def calcular_precio_final(self) -> float:
        if self.fasciculos:
            return self.precio + Papel.INCLUYE_FASCICULOS
        else:
            return self.precio

    def vender_kiosko(self, cantidad) -> bool:
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            self.vendidos += cantidad
            return True
        return False

    def calcular_ingresos_empresa(self) -> float:
        return self.vendidos * self.calcular_precio_final()

    def __str__(self) -> str:
        base = super().__str__()
        return (f"{base} | Precio: {self.precio} € | Stock: {self.cantidad} | Fasciculos: {'Si' if self.fasciculos else 'No'}")
    
if __name__ == "__main__":
    p = Papel("Hola", "Buenos dias", "Carlos López", datetime(2025, 12, 12), 1, "Alta", 200, 2.5, True, 10)
    print(p)
    print(f"Precio final: {p.calcular_precio_final()}")
    print()
    print(f"Ingresos: {p.calcular_ingresos_empresa()}")
    print()
    p.vender_kiosko(50)
    print(f"Después de vender 50 unidades")
    print(f"Cantidad: {p.cantidad} | Vendidos: {p.vendidos} | Ingresos : {p.calcular_ingresos_empresa()} €")
    print()
    print(f"Ingresos de la empresa: {p.calcular_ingresos_empresa()} €")