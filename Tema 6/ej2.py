from datetime import datetime

class Empleado:
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo

class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float):
        super().__init__(nombre, fecha_inicio, sueldo)
    
    def trienios(self) -> int:
        hoy = datetime.today()
        antiguedad_anos = (hoy - self.fecha_inicio).days // 365.25
        return antiguedad_anos // 3
    
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float, fecha_fin: datetime):
        super().__init__(nombre, fecha_inicio, sueldo)
        self.fecha_fin = fecha_fin

    def meses_restantes(self) -> int:
        hoy = datetime.today()
        diferencia = (self.fecha_fin.year - hoy.year) * 12 +(self.fecha_fin.month - hoy.month)
        return max(diferencia,0)
    
    def amplia_contrato(self, meses: int):
        nuevo_mes = self.fecha_fin.month + meses
        nuevo_anio = self.fecha_fin.year +(nuevo_mes - 1) // 12
        nuevo_mes = ((nuevo_mes - 1) % 12) + 1
        self.fecha_fin = datetime(nuevo_anio, nuevo_mes, self.fecha_fin.day)

if __name__ == "__main__":
    trabajador1 = EmpleadoFijo("Jose", datetime(2022, 6, 15), 2100)
    trabajador2 = EmpleadoTemporal("Jorge", datetime(2023, 1, 15), 1800, datetime(2026, 5, 15))
    
    print(f"Cantidad trienios empleado fijo: {trabajador1.trienios()}")

    print(f"Meses restantes: {trabajador2.meses_restantes()}")
    trabajador2.amplia_contrato(2)
    print(f"Tras ampliar, tiene {trabajador2.meses_restantes()} restantes")
