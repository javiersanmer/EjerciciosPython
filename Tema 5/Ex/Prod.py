from datetime import date


class Producto:
    def __init__(
        self,
        id: int,
        nombre: str,
        precio: float,
        categoria: str,
        fecha_caducidad: date,
        stock: int,
        proveedores: list[str],
        descuentos: list[float] | None = None
    ):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.fecha_caducidad = fecha_caducidad
        self.stock = stock
        self.proveedores = proveedores
        self.descuentos = descuentos if descuentos is not None else []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Producto):
            return False
        return self.id == other.id

    def __gt__(self, other) -> bool:
       return self.precio > other.precio

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"