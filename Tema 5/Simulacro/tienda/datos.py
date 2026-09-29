from datetime import date, timedelta
from ej1 import Animal


def get_animales():
    hoy = date.today()

    return [
        Animal(
            id=1,
            nombre="Luna",
            especie="Perro",
            fecha_nacimiento=hoy - timedelta(days=200),
            fecha_ingreso=hoy - timedelta(days=47),   # EXACTAMENTE 47 días en tienda
            precio=300.0,
            vacunado=True,
            caracteristicas=["juguetón", "pequeño"]
        ),
        Animal(
            id=2,
            nombre="Max",
            especie="Gato",
            fecha_nacimiento=hoy - timedelta(days=800),
            fecha_ingreso=hoy - timedelta(days=10),
            precio=150.0,
            vacunado=False,
            caracteristicas=["tranquilo", "independiente"]
        ),
        Animal(
            id=3,
            nombre="Rocky",
            especie="Conejo",
            fecha_nacimiento=hoy - timedelta(days=500),
            fecha_ingreso=hoy - timedelta(days=250),  # Más de 180 días
            precio=80.0,
            vacunado=True,
            caracteristicas=["blanco", "pequeño"]
        ),
        Animal(
            id=4,
            nombre="Nina",
            especie="Perro",
            fecha_nacimiento=hoy - timedelta(days=1200),
            fecha_ingreso=hoy - timedelta(days=30),
            precio=500.0,
            vacunado=True,
            caracteristicas=["grande", "protector"]
        ),
        Animal(
            id=5,
            nombre="Kiwi",
            especie="Loro",
            fecha_nacimiento=hoy - timedelta(days=1500),
            fecha_ingreso=hoy - timedelta(days=90),
            precio=250.0,
            vacunado=False,
            caracteristicas=["hablador", "verde"]
        ),
    ]