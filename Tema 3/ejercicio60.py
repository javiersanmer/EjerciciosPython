precios = {}
cantidad = {}
suma = 0

n = int(input("Cuántos productos hay en total?"))

for _ in range(n):
    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    canti = float(input("Cuántos de estos tienes?: "))
    precios[producto] = precio
    cantidad[producto] = cantidad


print("Cantidad de los productos: ")
for producto, cantidad in cantidad.items():
    print(f"{producto} : {canti}")

print("Precio de los productos: ")
for producto, precio in precios.items():
    print(f"{producto} : {precio}")

for producto in precios:
    suma += precios[producto]
media = suma / len(precios)

print(f"El precio medio de la tienda es: {media}")
