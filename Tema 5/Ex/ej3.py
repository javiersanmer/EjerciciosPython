from Prod import Producto
from datetime import date
from datos import get_productos

#Devuelve el precio  medio.
def f3a(productos: list[Producto]) -> float:
    return sum(p.precio for p in productos) / len(productos)

#Producto más caro
def f3b(productos: list[Producto]) -> Producto:
    #return max([p for p in productos], key=lambda e:e.precio)
    return max(productos) #para gt
    #return max(empleados) para ge

#Productos con precio mayor que n.
def f3c(productos: list[Producto], n: float) -> list[Producto]:
    return [p for p in productos if p.precio > n]

#Productos que valgan más que la media.
def f3d(productos: list[Producto]) -> list[Producto]:
    return [p for p in productos if p.precio > (sum(p.precio for p in productos) / len(productos))]
    #return [p for p in productos if p.precio > f3a(datos))]

#Producto con mayor stock.
def f3e(productos: list[Producto]) -> Producto:
    return max([p for p in productos], key=lambda e:e.stock)

#Productos de una categoría.
def f3f(productos: list[Producto], categoria: str) -> list[Producto]:
    return [p for p in productos if categoria in p.categoria]

#Productos caducados.
def f3g(productos: list[Producto]) -> list[Producto]:
    hoy = date.today()
    return [p for p in productos if hoy > p.fecha_caducidad]

#Productos de un proveedor concreto.
def f3h(productos: list[Producto], proveedor: str) -> list[Producto]:
    return [p for p in productos if proveedor in p.proveedores]

#Diccionario categoría → número de productos.
def f3i(productos: list) -> dict[str, int]:
    res = {}
    for p in productos:
        cat = p.categoria
        res[cat] = res.get(cat, 0) + 1
    return res

#Diccionario categoría → precio medio.
def f3j(productos: list) -> dict[str, int]:
    acumulado = {}
    conteo = {}

    for p in productos:
        cat = p.categoria
        acumulado[cat] = acumulado.get(cat, 0) + p.precio
        conteo[cat] = conteo.get(cat, 0) + 1

    return {cat: acumulado[cat] / conteo[cat] for cat in acumulado}


def f3k_valor_total_categoria(productos: list[Producto]) -> dict[str, float]:
    """Devuelve un diccionario {categoria: valor_total}, donde valor_total = precio*stock sumado"""
    res = {}
    for p in productos:
        res[p.categoria] = res.get(p.categoria, 0) + p.precio * p.stock
    return res

def f3l_producto_mas_valioso(productos: list[Producto]) -> Producto:
    """Devuelve el producto con mayor valor total (precio*stock)"""
    return max(productos, key=lambda p: p.precio * p.stock)

if __name__ == "__main__":

    datos = get_productos()

    print("===== f3a Precio medio =====")
    print(f3a(datos))
    print()

    print("===== f3b Producto más caro =====")
    r3b = f3b(datos)
    print(f'{r3b.nombre} - {r3b.precio} €')
    print()
    
    print("===== f3c Productos con precio mayor que n =====")
    r3c = f3c(datos,1)
    for e in r3c:
        print(f"{e.nombre} -- {e.precio}")

    print("===== f3d → Productos que valgan más que la media.. =====")
    r3e = f3e(datos)
    print(f'{r3e.nombre} - {r3e.precio} €')
    print()
    
    print("===== f3e → Producto con mayor stock.. =====")
    r3e = f3e(datos)
    print(f'{r3e.nombre} - {r3e.precio} €')
    print()

    print("===== f3f Productos de una categoría. =====")
    r3f = f3f(datos, "Limpieza")
    for e in r3f:
        print(f'{e.nombre} - {e.precio} €')
    print()
    
    print("===== f3g Productos caducados =====")
    r3g = f3g(datos)
    for e in r3g:
        print(f'{e.nombre} - {e.precio} €')
    print()

    print("===== f3h Productos proveedor concreto =====")
    r3h = f3h(datos, "Central Lechera")
    for e in r3h:
        print(f'{e.nombre} - {e.precio} €')
    print()

    print("===== f3i Reporte número de productos =====")
    print(f3i(datos))
    print()

    print("===== f3j Reporte número precio medio =====")
    print(f3j(datos))
    print()

    print("=====  Valor total por categoria =====")
    totales = f3k_valor_total_categoria(datos)
    for cat, val in totales.items():
        print(f"{cat} -> {val:.2f} €")

    print("=====  Mas valioso =====")
    p = f3l_producto_mas_valioso(datos)
    print(f"Producto más valioso: {p.nombre} ({p.categoria}) - Valor: {p.precio*p.stock:.2f} €")