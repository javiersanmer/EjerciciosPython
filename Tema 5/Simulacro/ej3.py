from Empleado import Empleado
from datetime import datetime
from datos import get_empleados

def f3a(empleados: list[Empleado]) -> float:
    return sum(e.sueldo for e in empleados) / len(empleados)

def f3b(empleados: list[Empleado]) -> Empleado: #Cuiddado si la clase lleva sobrecargados los max y min, si es asi solo pondríamos max sin lambda
    return max([e for e in empleados], key=lambda e:e.sueldo).nombre
    #return max(empleados).nombre para gt
    #return max(empleados) para ge
def f3c(empleados: list[Empleado], n: float) -> list[Empleado]:
    return [e for e in empleados if e.sueldo > n]

def tiempo_pasado(nacimiento: datetime) -> int:
   hoy = datetime.now()
   # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
   tiempo = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
   return tiempo

def f3d(empleados: list[Empleado], n: int) -> list[Empleado]:
    return [e for e in empleados if tiempo_pasado(e.fecha_ingreso) > n]

def f3e(empleados: list[Empleado]) -> Empleado:
    return min([e for e in empleados], key=lambda e:e.fecha_ingreso)

def f3f(empleados: list[Empleado]) -> list[Empleado]:
    return sorted(empleados, key=lambda e:e.fecha_ingreso)

def f3g(empleados: list[Empleado], anio: int) -> list[Empleado]:
    return [e for e in empleados if e.fecha_ingreso.year == anio] 

def f3h(empleados: list[Empleado], departamento: str) -> list[Empleado]:
    return [e for e in empleados if departamento in e.departamentos] 

# f3i) Reporte {departamento: número de empleados}
def f3i(empleados: list) -> dict[str, int]:
    reporte = {}
    for e in empleados:
        for d in e.departamentos:
            reporte[d] = reporte.get(d, 0) + 1
    return reporte


# f3j) Reporte {departamento: sueldo medio}
def f3j(empleados: list) -> dict[str, float]:
    acumulado = {}
    conteo = {}

    for e in empleados:
        for d in e.departamentos:
            acumulado[d] = acumulado.get(d, 0) + e.sueldo
            conteo[d] = conteo.get(d, 0) + 1

    return {d: acumulado[d] / conteo[d] for d in acumulado}
datos = get_empleados()
print("=== f3a Sueldo medio ====")
print(f3a(datos))

print("==== f3b Sueldo más alto ====")
r3b = f3b(datos)
print(f"{r3b} -- {r3b}")

print("==== f3c Sueldos > 2000 ====")
r3c = f3c(datos, 2000)

print("==== f3d Más de 3 años en empresa ====")
r3d = f3d(datos,3)
for e in r3d:
    print(f"{e.nombre} -- {e.fecha_ingreso}")

print("==== f3e Empleado más antiguo ====")
r3e = f3e(datos)
print(r3e)

print("==== f3f Ordenados por antiguedad ====")
r3f = f3f(datos)
for e in r3f:
    print(f"{e.nombre} -- {e.fecha_ingreso}")

print("==== f3g Contrados en año concreto(2022) ====")
r3g = f3g(datos, 2022)
for e in r3g:
    print(f"{e.nombre} -- {e.fecha_ingreso}")

print("===== f3h Departamento IT =====")
for e in f3h(datos, "IT"):
    print(e)
print()

print("===== f3i Reporte número empleados por departamento =====")
print(f3i(datos))
print()

print("===== f3j Reporte sueldo medio por departamento =====")
print(f3j(datos))