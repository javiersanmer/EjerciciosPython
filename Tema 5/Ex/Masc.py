# Mascota.py
from datetime import date

class Mascota:

    def __init__(self, id: int, nombre: str, especie: str,
                 fecha_nacimiento: date, peso: float, vacunas:  list[str] | None = None):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.vacunas = vacunas if vacunas is not None else []

    def __eq__(self, other) -> bool:
        if isinstance(other, Mascota):
            return self.id == other.id
        return False
    
    def edad(self) -> int:
        hoy = date.today()
        dias = (hoy - self.fecha_nacimiento).days
        return dias // 365
    
    def es_mayor_edad(self) -> bool:
        return self.edad() > 7
    
    def tiene_vacuna(self, vacuna: str) -> bool:
        return vacuna in self.vacunas

if __name__ == "__main__":
    from datetime import date, timedelta

    hoy = date.today()  # IMPORTANTE: con ()

    m1 = Mascota(1, "Luna", "Perro", hoy - timedelta(days=8*365), 12.5, ["Rabia"])
    m2 = Mascota(2, "Michi", "Gato", hoy - timedelta(days=3*365), 4.2, [])
    m3 = Mascota(1, "Otra", "Perro", hoy - timedelta(days=8*365), 10.0, [])

    print(m1)
    print(f"Edad:, {m1.edad()}")
    print("Es mayor:", m1.es_mayor_edad())
    print("Tiene vacuna Rabia:", m1.tiene_vacuna("Rabia"))