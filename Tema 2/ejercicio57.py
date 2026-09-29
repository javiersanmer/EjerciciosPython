def tablaMul(tabla : int) -> int:
    for i in range(1, 11):
        print(f"{tabla} * {i} = {tabla * i}")


for i in range(1,11):
    print(f"Tabla del {i}: ")
    
tabla = int(input("Introduce la tabla que quieres: "))
tablaMul(tabla)
