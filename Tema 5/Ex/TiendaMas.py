# TiendaMascotas.py
from Masc import Mascota
from datetime import date

class TiendaMascotas:

    def __init__(self, id: int, direccion: str, mascotas: list[Mascota] | None = None):
        self.id = id
        self.direccion = direccion
        self.mascotas = mascotas if mascotas is not None else []

    def total_mascotas(self) -> int:
        return len(self.mascotas)

    def anadir_mascota(self, m: Mascota) -> None:
        self.mascotas.append(m)

    def eliminar_mascota(self, id_mascota: int) -> bool:
        for m in self.mascotas:
            if m.id == id_mascota:
                self.mascotas.remove(m)
                return True
        return False

    def mascotas_por_especie(self, especie: str) -> list[Mascota]:
        return [m for m in self.mascotas if m.especie == especie]
    
    def mascotas_vacunadas(self) -> list[Mascota]:
        return [m for m in self.mascotas if m.vacunas]

    def mascotas_adultas(self) -> list[Mascota]:
        return [m for m in self.mascotas if m.es_mayor_edad()]

    def mascotas_por_especie(self, especie: str) -> list[Mascota]:
        return [m for m in self.mascotas if m.especie == especie]

    def mascotas_en_rango_edad(self, min_edad: int, max_edad: int) -> list[Mascota]:
        return [m for m in self.mascotas if min_edad <= m.edad() <= max_edad]
        
    def mascotas_en_rango_peso(self, minimo: float, maximo: float) -> list[Mascota]:
        return [m for m in self.mascotas if minimo <= m.peso <= maximo]

    def promedio_peso(self) -> float:
        if not self.mascotas:
            return 0.0
        total = sum(m.peso for m in self.mascotas)
        return total/len(self.mascotas)

    def mascotas_sin_vacuna(self, vacuna: str) -> list[Mascota]:
         return [m for m in self.mascotas if vacuna not in m.vacunas]
   
    def reporte_por_especie(self) -> dict[str, int]:
        d = {}
        for m in self.mascotas:
            d[m.especie] = d.get(m.especie, 0) + 1
        return d

    def reporte_vacunacion(self) -> dict[str, int]:
        d = {}
        for m in self.mascotas:
            d[m.vacunas] = d.get(m.vacunas, 0) + 1
        return d

if __name__ == "__main__":
    from datos import get_mascotas
    from datetime import date, timedelta

    lista = get_mascotas(0)
    hoy = date.today()
    tienda = TiendaMascotas(1, "Calle Mayor 5", lista)
    print("=== ESTADO INICIAL ===")

    print(f"Total:, {tienda.total_mascotas()}")

    print("Eliminando mantecado con id 2...")
    print(f"Elimina mascosta, {tienda.eliminar_mascota(2)}")
    print(f"Total tras eliminar:, {tienda.total_mascotas()}")
    

    print("Añadiendo nuevo mantecado...")

    hoy = date.today()

    nuevo = Mascota(1, "Joseador", "PerroOno", hoy - timedelta(days=2*365), 12.5, ["Joseador"])

    tienda.anadir_mascota(nuevo)

    print(f"Total tras añadir, {tienda.total_mascotas()}")
    print()
    print(f"Vacunadas:")
    for m in tienda.mascotas_vacunadas():
        print(f"{m.id}. {m.nombre}")
    print()
    print("Adultas:")
    for m in tienda.mascotas_adultas():
        print(f"{m.id}. {m.nombre}")
    print()
    print("Por especie: ")
    for m in tienda.mascotas_por_especie("Perro"):
        print(f"{m.id}. {m.nombre}")
    print()
    print("Por rango edad:")
    for m in tienda.mascotas_en_rango_edad(2,5):
        print(f"{m.id}. {m.nombre}")
    print()
    print("Por rango peso:")
    for m in tienda.mascotas_en_rango_peso(2,10):
        print(f"{m.id}. {m.nombre}")
    
    print()
    print(f"Promedio peso: {tienda.promedio_peso()}")

    print()
    print("Mascotas sin vacuna: ")
    for m in tienda.mascotas_sin_vacuna("Rabia"):
        print(f"{m.id}. {m.nombre}")

    print("===== REPORTE POR ESPECIE =====")
    for esp, cantidad in tienda.reporte_por_especie().items():
        print(esp, "->", cantidad)
    print()

    # Reporte por tipo
    print("===== REPORTE POR VACUNACIÓN =====")
    def reporte_vacunacion(self) -> dict[str, int]:
        d = {}
        for m in self.mascotas:
            for vac in m.vacunas:  # recorremos la lista de vacunas
                d[vac] = d.get(vac, 0) + 1
        return d