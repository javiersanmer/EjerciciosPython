from datetime import datetime
class Periodico:
    def __init__(self, nombre: str, titular: str, autor: str, fecha_salida: datetime) -> None:
        self.nombre = nombre
        self.titular = titular
        self.fecha_salida = fecha_salida
        self.autor = autor

    def filtrar_autor(self, autor_ingresado) -> bool:
        return self.autor == autor_ingresado
    
    def cambiar_titular(self, nuevo) -> None:
        self.titular = nuevo

    def duracion_lectura(self, num_palabras) -> float:
        return num_palabras / 200

    def lanzados_fecha(self, fecha) -> list[str]:
        titulares = []
        if self.fecha_salida < fecha:
            titulares.append(self.titular) 
        return titulares

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} | Titular: {self.titular} | Autor: {self.autor}")

if __name__ == "__main__":
    p = Periodico("Hola", "Buenos dias", "Carlos López", datetime(2025, 12, 12))
    print(p)
    print()
    print(f"¿Es de Carlos?: {p.filtrar_autor("Carlos López")}")
    print()
    print(f"Tiempo de lectura estimado: {p.duracion_lectura(600)} minutos")
    print()
    print(f"Titulares lanzados antes del 2026: {p.lanzados_fecha(datetime(2026, 1, 1))}")
    p.cambiar_titular("Buenas noches")
    print() 
    print(f"Cambio titular a 'Buenas noches': {p.titular}")
