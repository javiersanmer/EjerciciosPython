from pathlib import Path

def leer_contador(nombre_archivo: Path) -> int:
    # Si no existe, crear e inicializar
    if not nombre_archivo.exists():
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("0")

    # Leer contenido
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        try:
            contenido = f.read().strip()
            if contenido == "":
                contador = 0
            else:
                contador = int(contenido)
        except:
            contador = 0

    # Asegurar que el fichero tenga un valor válido
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(str(contador))

    return contador


def simular(contador: int, nombre_archivo: Path):
    while True:
        usuarioIntroduce = input("Pulsa Enter para sumar o 's' para salir: ")

        if usuarioIntroduce.lower() == "s":
            break

        contador += 1
        print(f"Nuevo valor: {contador}")

        # Guardar sobrescribiendo
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(str(contador))

    # Guardar al salir
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(str(contador))


if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent / "contador.txt"
    contador = leer_contador(nombre_archivo)
    print(f"Contador actual: {contador}")
    simular(contador, nombre_archivo)