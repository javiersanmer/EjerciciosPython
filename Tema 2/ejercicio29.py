usuario = input("Introduce tu usuario: ")

while True:
    contrasenia = input("Introduce tu contraseña: ")
    Repcontrasenia = input("Vuelve a introducir tu contraseña: ")

    if contrasenia == Repcontrasenia:
        print("Usuario creado")
        break

    print("Contraseña incorrecta")

