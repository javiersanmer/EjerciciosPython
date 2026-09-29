from datetime import date, timedelta
from Masc import Mascota
from Prod import Producto


# =========================
# MASCOTAS
# =========================

def get_mascotas(n: int) -> list[Mascota] | None:
    hoy = date.today()

    datos = [
        [
            Mascota(1, "Luna", "Perro", hoy - timedelta(days=8*365), 12.5, ["Rabia"]),
            Mascota(2, "Michi", "Gato", hoy - timedelta(days=3*365), 4.2, []),
            Mascota(3, "Rocky", "Perro", hoy - timedelta(days=1*365), 9.0, ["Moquillo"]),
            Mascota(4, "Kiwi", "Pajaro", hoy - timedelta(days=2*365), 0.5, []),
            Mascota(5, "Thor", "Perro", hoy - timedelta(days=10*365), 30.0, ["Rabia", "Parvovirus"]),
            Mascota(6, "Nina", "Gato", hoy - timedelta(days=6*365), 3.8, ["Leucemia"]),
            Mascota(7, "Toby", "Conejo", hoy - timedelta(days=4*365), 2.1, []),
            Mascota(8, "Simba", "Gato", hoy - timedelta(days=12*365), 5.0, ["Leucemia", "Rabia"]),
            Mascota(9, "Max", "Perro", hoy - timedelta(days=5*365), 15.0, ["Parvovirus"]),
            Mascota(10, "Kira", "Perro", hoy - timedelta(days=9*365), 18.0, []),
        ]
    ]


    return datos[n] if 0 <= n < len(datos) else None


# =========================
# PRODUCTOS
# =========================

def get_productos() -> list[Producto]:
    hoy = date.today()

    return [
        Producto(1, "Leche", 0.95, "Alimentacion", hoy + timedelta(days=7), 120, ["Central Lechera"]),
        Producto(2, "Pan", 1.10, "Alimentacion", hoy + timedelta(days=2), 80, ["Panificadora SA"]),
        Producto(3, "Detergente", 3.50, "Limpieza", hoy + timedelta(days=365), 60, ["CleanCorp"]),
        Producto(4, "Manzanas", 2.20, "Fruta", hoy + timedelta(days=5), 150, ["Frutas SL"]),
        Producto(5, "Yogur", 1.75, "Alimentacion", hoy - timedelta(days=2), 40, ["Central Lechera"]),
        Producto(6, "Lavavajillas", 2.80, "Limpieza", hoy + timedelta(days=400), 70, ["CleanCorp"]),
        Producto(7, "Platanos", 1.90, "Fruta", hoy + timedelta(days=6), 130, ["Frutas SL"]),
        Producto(8, "Carne", 6.50, "Alimentacion", hoy + timedelta(days=3), 50, ["Carnicas SA"]),
        Producto(9, "Arroz", 1.30, "Alimentacion", hoy + timedelta(days=200), 200, ["Distribuciones SA"]),
        Producto(10, "Ambientador", 4.25, "Limpieza", hoy + timedelta(days=500), 30, ["CleanCorp"]),
    ]