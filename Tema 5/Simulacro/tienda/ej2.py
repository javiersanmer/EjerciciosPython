from datetime import date
from datos import get_animales
from ej1 import Animal
class Tienda:
    def __init__(self, id: int, nombre: str, direccion: str, animales: list[Animal] | None = None) -> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        if animales is None:
            self.animales = []
        else:
            self.animales = animales

    def total_animales(self) -> int:
        return len(self.animales)
    
    def valor_total_stock(self) -> float:
        return sum(a.precio for a in self.animales)
    
    def anadir_animal(self, a: Animal) -> None:
        return self.animales.append(a)
    
    def vender_animal(self, id_animal: int) -> Animal | None:
        for a in self.animales:
            if a.id == id_animal:
                self.animales.remove(a)
                return a
            return False
        
    def animales_por_especie(self, especie: str) -> list[Animal]:
        resultado = []
        for a in self.animales:
            if a.especie == especie:
                resultado.append(a)
            return resultado
        
    def animales_no_vacunados(self) -> list[Animal]:
        return [a for a in self.animales if a not in a.vacunado]

    def cachorros(self) -> list[Animal]:
        return [a for a in self.animales if a in a.es_cachorro()]
    
from datetime import date
from datos import get_animales
from ej1 import Animal


class Tienda:

    def __init__(self, id: int, nombre: str, direccion: str,
                 animales: list[Animal] | None = None) -> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.animales = animales if animales is not None else []

    #EN EL EXAMEN HAY LAMBDAAAAAA

    def total_animales(self) -> int:
        return len(self.animales)

    def valor_total_stock(self) -> float:
        return sum(a.precio for a in self.animales)

    def anadir_animal(self, a: Animal) -> None:
        # Evitar duplicados por ID
        if not any(x.id == a.id for x in self.animales):
            self.animales.append(a)

    def vender_animal(self, id_animal: int) -> Animal | None:
        for a in self.animales:
            if a.id == id_animal:
                self.animales.remove(a)
                return a
        return None

    # -------------------------
    # FILTRADOS
    # -------------------------

    def animales_por_especie(self, especie: str) -> list[Animal]:
        return [a for a in self.animales if a.especie == especie]

    def animales_no_vacunados(self) -> list[Animal]:
        return [a for a in self.animales if not a.vacunado]

    def cachorros(self) -> list[Animal]:
        return [a for a in self.animales if a.es_cachorro()]

    def animales_en_rango_precio(self, minimo: float, maximo: float) -> list[Animal]:
        return [a for a in self.animales if minimo <= a.precio <= maximo]

    def reporte_por_especie(self) -> dict[str, int]:
        reporte = {}
        for a in self.animales:
            if a.especie in reporte:
                reporte[a.especie] += 1
            else:
                reporte[a.especie] = 1
        return reporte

    def reporte_valor_por_especie(self) -> dict[str, float]:
        reporte = {}
        for a in self.animales:
            if a.especie in reporte:
                reporte[a.especie] += a.precio
            else:
                reporte[a.especie] = a.precio
        return reporte

    def animal_mas_antiguo_en_tienda(self) -> Animal | None:
        if not self.animales:
            return None
        return max(self.animales, key=lambda a: a.dias_en_tienda())
    
if __name__ == "__main__":
    animales = get_animales()
    tienda = Tienda(1, "Animalia", "Calle Mayor 10", animales)

    print(f"Total animales: {tienda.total_animales()}")
    print("Total animales:", tienda.total_animales())
    print("Valor total stock:", tienda.valor_total_stock())

    print("No vacunados:", tienda.animales_no_vacunados())
    print("Cachorros:", tienda.cachorros())

    print("Rango precio 100-400:",
          tienda.animales_en_rango_precio(100, 400))

    print("Reporte por especie:", tienda.reporte_por_especie())
    print("Valor por especie:", tienda.reporte_valor_por_especie())

    print("Animal más antiguo en tienda:",
          tienda.animal_mas_antiguo_en_tienda())