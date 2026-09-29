from funcs import login, menuElige

usuarioLogueado = login()
if usuarioLogueado is not None:
    menuElige(usuarioLogueado)
    print("Has salido de la tienda.")
else:
    print("No se ha podido iniciar sesión.")
