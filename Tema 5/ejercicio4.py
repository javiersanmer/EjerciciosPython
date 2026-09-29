from dataclasses import dataclass
from datetime import datetime

@dataclass
class Proveedor:
    id_proveedor: int
    nombre: str
    telefono: str
    email: str
    localidad: str
    
@dataclass
class Pedido:
    id_pedido: int
    fecha_pedido: datetime
    fecha_entrega: datetime
    precio_total: float
    direccion_envio: str
    peso_kg: float
    tipo_producto: str
    id_proveedor: int

"""1:1 from dataclasses import dataclass

@dataclass
class Pasaporte:
    numero: str
    pais: str

@dataclass
class Persona:
    nombre: str
    edad: int
    pasaporte: Pasaporte  # Relación 1:1"""