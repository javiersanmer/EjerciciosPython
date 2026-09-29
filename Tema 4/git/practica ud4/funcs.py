from datos import get_juegos, get_usuarios
from Videojuego import Videojuego
from Usuario import Usuario

def login() -> Usuario:
    usuarios = get_usuarios()
    usuObj = None
    salir = False
    while not salir:
        usuarioIntroduce = input("Login: ")
        while True:
            for u in usuarios:
                if u.nombre == usuarioIntroduce:
                    usuObj = u
            if usuObj is None:
                print("El nombre de usuario no existe")
                usuarioIntroduce = input("Inserte de nuevo el nombre: ")
            else:
                break
        intentos = 0
        constrasenia = input("Contraseña: ")
        while not salir and intentos < 3:
            if constrasenia == usuObj.contra:
                salir = True
            else:
                intentos += 1
                if intentos < 3:
                    constrasenia = input("Contraseña incorrecta, inserte de nuevo la contraseña: ")
                if intentos >= 3:
                    print("Demasiados intentos")
                    salir = True

    if intentos < 3:
        return usuObj

def menuMostrar(usuario: Usuario) -> list[Videojuego]:
    juegos = get_juegos()
    juegosDispo = []
    print("JUEGOS DISPONIBLES PARA COMPRAR: ")

    for juego in juegos:
        if juego not in carrito and juego not in compras and usuario.edad() >= juego.PEGI:
            juegosDispo.append(juego)
            precio = juego.precio_final(0.21, 0)
            print(f"{[len(juegosDispo)]}. {juego.nombre}, precio: {precio:.2f}")
    if not juegosDispo:
        print("No hay juegos disponibles")

    print("------------------------")
    print("")
    print(f"Actualmente tienes {usuario.saldo:.2f} €")
    print("-------------------------")

    return juegosDispo

def ingresaSaldo(usuario: Usuario) -> float:
    cantidad = float(input("Cantidad a ingresar: "))
    while cantidad < 0:
        print("Cantidad no válida")
        cantidad = float(input("Cantidad a ingresar: "))
    
    cantidad = round(cantidad,2)
    usuario.saldo += cantidad
    return cantidad

def menuElige(usuario: Usuario) -> None:
    salirTienda = False
    while not salirTienda:
        juegos = menuMostrar(usuario)
        print("[V]er mis juegos")
        print("[I]ngresar dinero")
        print("Ir al [c]arrito")
        print("[S]salir")
        
        menuOpcion = input("¿Qué quieres hacer?").upper()
        print("------------------------")
        
        if menuOpcion == "I":
            nuevoSaldo = ingresaSaldo(usuario)
            print(f"Enhorabuena has ingresado: {nuevoSaldo:.2f} €")
            input()
        elif menuOpcion == "C":
            print("Tienes los siguientes juegos en el carrito: ")
            mostrarCarrito(usuario)
            input()
        elif menuOpcion == "V":
            print("Tienes los siguientes juegos: ")
            if len(compras) == 0:
                print("No tienes juegos")
                input()
            else:
                for j in compras:
                    print(j.nombre)
            input()            
        elif menuOpcion.isdigit():
            num = int(menuOpcion)
            if num >= 1 and num <= len(juegos):
                juego = juegos[num -1]
                mostrarDetallesJuego(juego)
            else:
                print("Opcion no valida")
                input()

        elif menuOpcion == "S":
            print("Fin del programa")
            salirTienda =True
            break

def mostrarDetallesJuego(juego: Videojuego) -> None:
    print(juego)
 
    aniadirJuego = input("¿Quieres añadir el juego al carrito (S/N)?").upper()
    if aniadirJuego == "S":
        if juego not in carrito:
            carrito.append(juego)
            print(f"{juego.nombre} añadido al carrito")
        else:
            print("El juego ya está en el carrito")
    input()

carrito = []
def mostrarCarrito(usuario: Usuario) -> None: 
    if len(carrito) == 0:
        print(f"El carrito está vacío.")
        input()
    else:
        total = 0
        for juego in carrito:
            precio = juego.precio_final(0.21, 0)
            total += precio
            print(f"{juego.nombre} -- precio: {precio:.2f}")

        print(f"El precio total es: {total:.2f}")
        print("[P]agar")
        print("[V]olver")
        opcionElegida = input().upper()

        if opcionElegida == "P":
            pagarCarrito(usuario)

compras = []
def pagarCarrito(usuario: Usuario) -> None: 
    total = 0
    for juego in carrito:
        total += juego.precio_final(0.21, 0)
       
    if usuario.saldo >= total:
        usuario.saldo -= total
        compras.extend(carrito)
        carrito.clear()
            
        print("Compra completada")
    else:
        print("No tienes saldo suficiente")