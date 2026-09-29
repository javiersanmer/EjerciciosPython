from datetime import datetime

class Coche:
    def __init__(self, marca : str, modelo : str, anio_fabricacion : int, peso : int, tipo_motor : str, potencia : str, automatico : bool, num_puertas : int, num_asientos : int, consumo : float, deposito : float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.deposito = deposito
    
    def __str__(self) -> str:
        return(
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}, "
            f"Año de fabricación: {self.anio_fabricacion}, "
            f"Peso: {self.peso}, "
            f"Tipo motor: {self.tipo_motor}, "
            f"Potencia: {self.potencia}, "
            f"Automático: {self.automatico}, "
            f"Número de puertas: {self.num_puertas}, "
            f"Número de asientos: {self.num_asientos}, "
            f"Consumo: {self.consumo}, "
            f"Depósito: {self.deposito}, "
        )
    
    def autonomia(self) -> float:
        return (self.deposito / self.consumo) * 100
    
    def __lt__(self, other):
        return self.potencia < other.potencia

    def __gt__(self, other):
        return self.potencia < other.potencia
    
    def __eq__(self, other):
        if isinstance(other, Coche):
            return(
                self.marca == other.marca and
                self.modelo == other.modelo and 
                self.anio_fabricacion == other.anio_fabricacion and
                self.peso == self.peso and
                self.tipo_motor == other.tipo_motor and 
                self.potencia == other.potencia and
                self.automatico == other.automatico and
                self.num_puertas == other.num_puertas and
                self.num_asientos == other.num_asientos and 
                self.consumo == other.consumo and
                self.deposito == other.deposito
            )
