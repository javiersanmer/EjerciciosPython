class Cuenta:
    COMISION = 5.0 #si es porcentual se hace con regla de 3.

    def __init__(self, titular: str, numero_cuenta:str, saldo: float):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __eq__(self, other) -> bool:
        if isinstance(other, Cuenta):
            return self.numero_cuenta == other.numero_cuenta
        return False

    def __hash__(self):
        return hash(self.numero_cuenta)
    
    def __str__(self):
        return f"Cuenta | Titular: {self.titular} | Nº: {self.numero_cuenta} | Saldo: {self.saldo:.2f}€"
    
    def ingresar(self, cantidad:float):
        self.saldo += cantidad
    
    def retirar(self, cantidad: float) -> bool:
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    
    def cobrar_comision(self):
        self.saldo -= Cuenta.COMISION