from datetime import date

class Mantecado:
    def __init__(self, id: int, tipo: str, fecha_creacion: date, fecha_caducidad: date, precio: float, ingredientes: list[str]) -> None:
        self.id = id
        self.tipo = tipo 
        self.fecha_creacion = fecha_creacion
        self.fecha_caducidad = fecha_caducidad
        self.precio = precio
        self.ingredientes = ingredientes
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Mantecado):
            return self.id == other.id
        return False
    
    def dias_para_caducar(self) -> int:
        hoy = date.today()
        diferencia = self.fecha_caducidad - hoy
        return diferencia.days
    
    def esta_caducado(self) -> bool:
        return self.dias_para_caducar() < 0
    
    def __str__(self):
        return f"{self.id} -- {self.tipo} -- {self.fecha_creacion} -- {self.fecha_caducidad} -- {self.precio} -- {self.ingredientes}"

if __name__ == '__main__':
    m1 = Mantecado(1, "Chocolate", date(2025, 1, 12),date(2025, 12, 31), 3.5, ["harina", "azúcar", "manteca", "cacao"])
    m3 = m1
    m3 = Mantecado(2, "Chocolate Especial", date(2025, 5, 12), date(2026, 1, 5), 4.0 ,["harina", "azúcar", "manteca", "cacao", "almendra"])
    
    print("Representación: ")
    print(m1)

    print("¿Está caducado?")
    print(m1.esta_caducado())

    print("Días para caducar: ")
    print(m1.dias_para_caducar())

    print("Comparacio por id (m1 == m2)")
    print(m1.id == m3.id)

        