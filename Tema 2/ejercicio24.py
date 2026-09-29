'''
usuario = input("Introduce tu usario: ")

contrasenia = input("Introduce tu contraseña: ")
repContrasenia = input("Vuelve a introducir tu contraseña: ")
while(contrasenia != repContrasenia):
    print("NO COINCIDEN")
    contrasenia = input("Introduce tu contraseña: ")
    repContrasenia = input("Vuelve a introducir tu contraseña: ")

print("Usuario creaado correctamente")
'''
usuario = input("Introduce tu usario: ")
constraseniaCorrecta = False

while not constraseniaCorrecta:
    contrasenia = input("Introduce tu contraseña: ")
    repContrasenia = input("Vuelve a introducir tu contraseña: ")

    if contrasenia == repContrasenia:
        constraseniaCorrecta = True
    else:
        print("NO COINCIDEN")
print("Usuario creaado correctamente")
