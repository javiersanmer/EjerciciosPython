tareasPendientes = ["Comprar fruta", "Estudiar programación", "Desisntalar el LOL"]
separador = "----------------------"

while True:
    print("Bienvenido a la app de listas to-do más avanzada del universo")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea pendiente")
    print("0. Salir")
    opcionMenu = int(input("Introduce una opción del menú: "))
    print(separador)

    if opcionMenu == 0:
        break 
        
    if opcionMenu == 1:
        if len(tareasPendientes) > 0:
            for i, tarea in enumerate(tareasPendientes):
                print(f"{i+1}.{tarea}")
            print(separador)
            tareasCompletadas = int(input("Selecciona las tareas finalizadas(0 para salir) "))
            if tareasCompletadas == 0:
                print("Espabila")
            elif tareasCompletadas > 0 and tareasCompletadas < len(tareasPendientes)+1:
                tareasPendientes.pop(tareasCompletadas-1)
                print("Ole tu")
                print(separador)
            elif tareasCompletadas > len(tareasCompletadas)+1:
                print("No valida")
                print(separador)

        else:
            print("No tienes tareas pendientes")
            print(separador)

    elif opcionMenu == 2:
        tarea = input("¿Qué tares quieres insertar?")
        posicion = int(input("Introduce la posición: "))

        inser = tareasPendientes.insert(posicion-1, tarea)
