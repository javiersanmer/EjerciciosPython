from datetime import date

class Animal:
    def __init__(self, id: int, nombre: str, especie: str, fecha_nacimiento: date, fecha_ingreso: date, precio: float, vacunado: bool, caracteristicas: list[str]) -> None:
        self.id = id
        self.nombre = nombre 
        self.especie = especie
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.precio = precio
        self.vacunado = vacunado
        self.caracteristicas = caracteristicas
    def __eq__(self, other) -> bool:
        if isinstance(other, Animal):
            return self.id == other.id
        return False
    
    def edad_en_dias(self) -> int:
        hoy = date.today()
        edad = hoy - self.fecha_nacimiento 
        return edad.days
    
    def dias_en_tienda(self) -> int:
        hoy = date.today()
        diasTienda = hoy - self.fecha_ingreso 
        return diasTienda.days
    
    def es_cachorro(self) -> bool:
        return self.edad_en_dias() < 365
    
    def necesita_revision(self) -> bool:
        if self.vacunado:
            return True
        else:
            return False
    def __str__(self) -> str:
        return f"{self.id} - {self.nombre} - {self.especie} - {self.fecha_nacimiento} - {self.fecha_ingreso} - {self.precio} - {self.vacunado} - {self.caracteristicas}"
    
if __name__ == "__main__":
    a1 = Animal(
        id=1,
        nombre="Luna",
        especie="Perro",
        fecha_nacimiento=date(2025, 10, 1),   # Menos de 1 año
        fecha_ingreso=date(2026, 1, 15),
        precio=300.0,
        vacunado=True,
        caracteristicas=["juguetón", "pequeño", "energético"]
        )
    a2 = Animal(
        id=2,
        nombre="Max",
        especie="Gato",
        fecha_nacimiento=date(2023, 5, 10),   # Más de 1 año
        fecha_ingreso=date(2026, 1, 10),
        precio=150.0,
        vacunado=False,
        caracteristicas=["tranquilo", "independiente"]
    )
    a3 = Animal(
        id=3,
        nombre="Rocky",
        especie="Conejo",
        fecha_nacimiento=date(2024, 3, 20),
        fecha_ingreso=date(2025, 6, 1),   # Más de 200 días en tienda
        precio=80.0,
        vacunado=True,
        caracteristicas=["tranquilo", "independiente"]
    )

    print(a1.edad_en_dias())
    print(a1.dias_en_tienda())
    print(a1.es_cachorro())
    print(a1.necesita_revision())