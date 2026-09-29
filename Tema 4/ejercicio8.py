from Planeta import Planeta
from datetime import datetime

planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna",1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4,1.60659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Júpiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.4819e23], ["Calisto", 2.410e6, 1.0759e23], ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titán", 2.576e5, 1.345e23], ["Rea", 1.527e6, 2.3166e21], ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, datetime.min, [["Caronte", 6.057e5, 1.586e21]])
]
planetas_trappist = [
    Planeta("TRAPPIST-1b",  0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

masaSistemaSolar = [planeta.masa for planeta in planetas]
mediaSolar = sum(masaSistemaSolar) / len(masaSistemaSolar)

masaTRAPPIST = [planeta.masa for planeta in planetas_trappist]
mediaTrappist = sum(masaTRAPPIST) / len(masaTRAPPIST)

print(f"El Solar tiene {mediaSolar} y TRAPPIST-1 tien {mediaTrappist}")

todosPlanetas = planetas + planetas_trappist

maxDensidad = max([p.get_densidad() for p in todosPlanetas])
nomMasDenso = todosPlanetas[0].nombre

densidadTierra = 0
for p in planetas:
    if p.nombre == "Tierra":
        densidad_tierra = p.get_densidad()
        break

parecidoPrimerPlaneta = planetas_trappist[0]
diferenciaPrimerPlaneta = abs(parecidoPrimerPlaneta.get_densidad() - densidad_tierra)

for p in planetas_trappist:
    diferenciaMin = abs(p.get_densidad() - densidad_tierra)
    if diferenciaMin < diferenciaPrimerPlaneta:
        diferenciaPrimerPlaneta = diferenciaMin
        masParecido = p

print(f"El planeta de TRAPPIST-1 cuya densidad más se parece a la Tierra es: {masParecido.nombre}")

sinLunasSolar = [p.nombre for p in planetas if not p.lunas ]
sinLunasTrappist =[p.nombre for p in planetas_trappist if not p.lunas]

print(f"Planetas del Solar sin lunas {sinLunasSolar}")
print(f"Planetas del Trappist sin lunas {sinLunasTrappist}")
