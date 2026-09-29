canciones_ana = ["Master of Puppets", "Painkiller", "Hallowed Be Thy Name", "Hallowed Be Thy Name", "Holy Wars", "Chop Suey!"]
canciones_luis = ["Painkiller", "Holy Wars", "Chop Suey!", "Walk", "Walk", "The Trooper"]

set_ana = set(canciones_ana)
set_luis = set(canciones_luis)

print("a) Eliminar elementos repetidos en ambas listas:")
cancionesAnaSinRepes = list(set(canciones_ana))
cancionesLuisSinRepes = list(set(canciones_luis))
print(f"Canciones que solo tiene Ana {cancionesAnaSinRepes} y Luis {cancionesLuisSinRepes}")
print("b) Mostrar las canciones que tienen ambos usuarios:", list(set_ana & set_luis))
print("c) Mostrar las canciones que tienen Ana pero no Luis :",list(set_ana - set_luis))
print("d) Indicar si alguno de los dos usuarios tiene canciones repetidas en sus listas originales :",len(set_ana) != len(set_ana))
print(" Indicar si alguno de los dos usuarios tiene canciones repetidas en sus listas originales :" , len(set_luis) != len(set_luis))
print("e) Obtener la playlist conjunta, es decir, todas las canciones que tiene Ana o Luis :",list(set_luis | set_ana))
print("f) Mostrar las canciones que tiene Luis pero no Ana",list(set_luis - set_ana))
