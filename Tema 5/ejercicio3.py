from dataclasses import dataclass
from datetime import datetime

@dataclass
class Pedido:
    id: int
    cantidad: float
    fecha: datetime
    id_cliente: int
    id_comercial: int
    
@dataclass
class Cliente:
    id: int
    nombre: str
    apellido1: str
    apellido2: str
    ciudad: str
    categoria: int