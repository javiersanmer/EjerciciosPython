from datetime import datetime, timedelta

class Vehiculo:
    def __init__(self, matricula : str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime):
        self.matricula = matricula
        self.marca = marca
        self.fecha_matriculacion = fecha_matriculacion
        self.fecha_ultima_itv = fecha_ultima_itv

class Coche(Vehiculo):
    def __init__(self, matricula : str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, num_puertas: int, combustible: str):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.num_puertas = num_puertas
        self.combustible = combustible

    def proxima_itv(self) -> datetime:
        hoy = datetime.today()
        dias_desde_matriculacion = (hoy - self.fecha_matriculacion).days

        if dias_desde_matriculacion < 4*365.25:
            return self.fecha_matriculacion + timedelta(days=4*365.25)
        elif dias_desde_matriculacion < 10 * 365.25:
            return self.fecha_ultima_itv + timedelta(days=2*365.25)
        else:
            return self.fecha_ultima_itv + timedelta(days=365.25)

class Moto(Vehiculo):
    def __init__(self, matricula : str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, cilindrada: int):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.cilindrada = cilindrada

    def proxima_itv(self) -> datetime:
        hoy = datetime.today()
        dias_desde_matriculacion = (hoy - self.fecha_matriculacion).days

        if dias_desde_matriculacion < 4 * 365.25:
            return self.fecha_matriculacion + timedelta(days=4 * 365.25)
        else:
            return self.fecha_ultima_itv + timedelta(days=2 *365.25)

        
if __name__ == "__main__":
    fecha_matriculacion_coche = datetime(2018, 6, 15)
    fecha_ultima_itv_coche = datetime(2024, 6, 15)

    fecha_matriculacion_moto = datetime(2021, 3, 10)
    fecha_ultima_itv_moto = datetime(2024, 3, 10)

    coche = Coche("1234ABC", "Toyota", fecha_matriculacion_coche, fecha_ultima_itv_coche, 5, "Gasolina")
    moto = Moto("5678XYZ", "Honda", fecha_matriculacion_moto, fecha_ultima_itv_moto, 600)
    
    print("Próxima ITV del coche:", coche.proxima_itv())
    print("Próxima ITV de la moto:", moto.proxima_itv())

#Práctica en tipo test

    print(isinstance(coche, Coche))
    print(isinstance(coche, Vehiculo))
    print(isinstance(moto, Moto))
    print(isinstance(moto, Vehiculo))
    print(isinstance(moto, object))
    print(isinstance(Moto, Coche))
    print(issubclass(Moto, Vehiculo))
    print(issubclass(Vehiculo, Moto))
    print(issubclass(Vehiculo, object)) #Si le entra clase siempre devuelve True.
    print(issubclass(None, object)) #Da error.