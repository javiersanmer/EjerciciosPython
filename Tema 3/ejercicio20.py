tareasPendientes = ["Comprar fruta", "Estudiar programación", "Desisntalar el LOL"]
separador = "----------------------"

while True:
    print("Bienvenido a la app de listas to-do más avanzada del universo")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea pendiente")
    print("0. Salir")

    opcionMenu = int(input("Introduce una opción del menú: "))

    if opcionMenu == 0:
        break 
        
    if opcionMenu == 1:
        for i, tarea in enumerate(tareasPendientes):
            print(f"{i+1}.{tarea}")
        print(separador)
    
    elif opcionMenu == 2:
        tarea = input("¿Qué tares quieres insertar?")
        posicion = int(input("Introduce la posición: "))

        inser = tareasPendientes.insert(posicion-1, tarea)
