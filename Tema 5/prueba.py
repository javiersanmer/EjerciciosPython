from datetime import datetime
from Portatiles import Portatil

portatil1 = Portatil(codigo="D13XPS", nombre="XPS 13", marca="Dell", pulgadas=13.3, modelo=["XPS9310", "XPS9300"], tactil=True, fecha_salida=datetime(2021, 3, 1), fecha_descontinuacion=datetime(2025, 12, 31), precio_venta=1499)

portatil2 = Portatil(codigo="MBP14", nombre="MacBook Pro 14", marca="Apple", pulgadas=14.2, modelo=["M1 Pro", "M1 Max"], tactil=False, fecha_salida=datetime(2021, 10, 18), fecha_descontinuacion=datetime(2026, 12, 31), precio_venta=2199)
 
print(portatil1)

print(portatil2)

print(f"¿Está descontinuado el {portatil1.nombre}?: {"Si" if portatil1.disponible() else "No"}")

print(f"Cambio de precio del {portatil1.nombre}: {portatil1.cambio_precio(2)}")

print(f"Tiene tactil el {portatil2.nombre}: {"Si" if portatil2.tactil else "No"}")

print(f"Es el {portatil1.nombre} más grande que {portatil2.nombre}: {"Si" if portatil1 > portatil2 else "No"}")



"""En el examen hacemos las pruebass en el bloque  __main__
if __name__ == "__main__":
    from random import randint
    i1 = Usuario(1, "Juan", "Lol")"""

"""
def __hash__:
    return self.id_portatil
para usar  conjuntos y diccionarios hay que sobrecargalos,
por ello usamos hash"""



#En javascript son un total de 20 lineas y mu facil

from datetime import date, timedelta
from ej1 import Mantecado

class Almacen:
    def __init__(self, id: int, direccion: str, mantecados: list[Mantecado] = None) -> None:
        self.id = id
        self.direccion = direccion
        if mantecados is None:
            self.mantecados = []
        else:
            self.mantecados = mantecados

    def total_mantecados(self) -> int:
        return len(self.mantecados)

    def aniadir_mantecado(self, m: Mantecado) -> None:
        self.mantecados.append(m)

    def eliminar_mantecado(self, m: Mantecado) -> None:
        if m in self.mantecados:
            self.mantecados.remove(m)

    def mantecados_caducados(self) -> list[Mantecado]:
        hoy = date.today()
        resultado = []
        for m in self.mantecados:
            if m.fecha_caducidad < hoy:
                resultado.append(m)
        return resultado

    def proximos_a_caducar(self, n: int) -> list[Mantecado]:
        hoy = date.today()
        limite = hoy + timedelta(days=n)
        resultado = []
        for m in self.mantecados:
            if hoy <= m.fecha_caducidad <= limite:
                resultado.append(m)
        return resultado

    def mantecados_en_rango_precio(self, minimo: float, maximo: float) -> list[Mantecado]:
        resultado = []
        for mantecado in self.mantecados:
            if minimo <= mantecado.precio <= maximo:
                resultado.append(mantecado)
        return resultado

    def sin_ingredientes(self, ingrediente: str) -> list[Mantecado]:
        resultado = []
        for mantecado in self.mantecados:
            if ingrediente not in mantecado.ingredientes:
                resultado.append(mantecado)
        return resultado

if __name__ == "__main__":
    from datos import get_mantecados

    almacen = Almacen(1, "Calle nse", get_mantecados(10))

    print("=== ESTADO INICIAL ===")
    print(f"Total mantecados: {almacen.total_mantecados()}")

    print("\n=== LISTADO COMPLETO ===")
    for m in almacen.mantecados:
        print(m)

    resultado = almacen.mantecados_caducados()
    print("\n=== CADUCADOS ===")
    for mantecado in resultado:
        print(mantecado)

    resultado = almacen.proximos_a_caducar(3)
    print("\n=== PRÓXIMOS A CADUCAR (<= 3 días) ===")
    for mantecado in resultado:
        print(mantecado)
