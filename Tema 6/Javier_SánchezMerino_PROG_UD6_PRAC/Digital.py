from datetime import datetime
from Periodico import Periodico

class Digital(Periodico):
    LIMITE_GRATIS = 5

    def __init__(self, nombre:str, titular:str, autor: str, fecha_salida:datetime, dominio:str, num_visitas:int, suscriptores:int, precio_suscripcion:float) -> None:
        super().__init__(nombre, titular, autor, fecha_salida)
        self.dominio = dominio
        self.num_visitas = num_visitas
        self.suscriptores = suscriptores
        self.precio_suscripcion = precio_suscripcion

    def requiere_suscripcion(self, visitas_usuario) -> float:
        return visitas_usuario > Digital.LIMITE_GRATIS

    def articulo_supera_visitas(self, visitas) -> str | None:
        superan = []
        if self.num_visitas >= visitas:
            superan.append(self.titular)
        return superan

    def calcular_ingresos_empresa(self, dias: int) -> float:
        meses = dias / 30
        return self.suscriptores * self.precio_suscripcion * meses

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Dominio: {self.dominio} | Precio Suscripción: {self.precio_suscripcion} €"

if __name__ == "__main__":
    p = Digital("Hola", "Buenos dias", "Carlos López", datetime(2025, 12, 12), "www.noticias.com", 10, 100, 5.0)
    print(p)
    print()
    print(f"¿Requiere suscripción?(6 visitas): {p.requiere_suscripcion(6)}")
    print(f"¿Requiere suscripción?(3 visitas): {p.requiere_suscripcion(3)}")
    print()
    print(f"¿Que articulos superan las 5 visitas? {p.articulo_supera_visitas(5)}")
    print()
    print(f"Ingresos de la empresa en 30 días: {p.calcular_ingresos_empresa(30)} €")