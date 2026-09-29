from Prod import Producto
from datos import get_productos

def categoria_mas_rentable(productos: list[Producto]) -> tuple[str, float]:
    """
    Devuelve la categoría más rentable y su valor total en stock
    """
    categorias = {}
    for p in productos:
        categorias.setdefault(p.categoria, []).append(p)

    valor_total = {}
    for cat, lista in categorias.items():
        valor_total[cat] = sum(p.precio * p.stock for p in lista)

    cat_mas_rentable = max(valor_total, key=lambda c: valor_total[c])
    return cat_mas_rentable, valor_total[cat_mas_rentable]

if __name__ == "__main__":
    productos = get_productos()
    cat, valor = categoria_mas_rentable(productos)
    print("===== CATEGORÍA MÁS RENTABLE =====")
    print(f"La categoría más rentable es: {cat} con un valor total de {valor:.2f} €")

def proveedor_mas_valioso(productos: list[Producto]) -> tuple[str, float]:
    valor = {}
    for p in productos:
        for prov in p.proveedores:
            valor[prov] = valor.get(prov, 0) + p.precio * p.stock
    prov_max = max(valor, key=lambda k: valor[k])
    return prov_max, valor[prov_max]

if __name__ == "__main__":
    productos = get_productos()
    prov, val = proveedor_mas_valioso(productos)
    print(f"Proveedor más valioso: {prov} con un valor total de {val:.2f} €")

def proveedor_mas_valioso(productos: list[Producto]) -> tuple[str, float]:
    valor = {}
    for p in productos:
        for prov in p.proveedores:
            valor[prov] = valor.get(prov, 0) + p.precio * p.stock
    prov_max = max(valor, key=lambda k: valor[k])
    return prov_max, valor[prov_max]

if __name__ == "__main__":
    productos = get_productos()
    prov, val = proveedor_mas_valioso(productos)
    print(f"Proveedor más valioso: {prov} con un valor total de {val:.2f} €")

def categoria_mas_cara(productos: list[Producto]) -> tuple[str, float]:
    acumulado = {}
    conteo = {}
    for p in productos:
        acumulado[p.categoria] = acumulado.get(p.categoria, 0) + p.precio
        conteo[p.categoria] = conteo.get(p.categoria, 0) + 1
    precios_medios = {cat: acumulado[cat]/conteo[cat] for cat in acumulado}
    cat_max = max(precios_medios, key=lambda c: precios_medios[c])
    return cat_max, precios_medios[cat_max]

if __name__ == "__main__":
    productos = get_productos()
    cat, precio = categoria_mas_cara(productos)
    print(f"La categoría más cara es: {cat} con un precio medio de {precio:.2f} €")

def top_productos_valor(productos: list[Producto], n: int) -> list[Producto]:
    return sorted(productos, key=lambda p: p.precio * p.stock, reverse=True)[:n]

if __name__ == "__main__":
    productos = get_productos()
    top3 = top_productos_valor(productos, 3)
    print("Top 3 productos por valor total:")
    for p in top3:
        print(f"{p.nombre} ({p.categoria}) - Valor: {p.precio * p.stock:.2f} €")