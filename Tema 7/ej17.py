from pathlib import Path

nombre_archivo = Path(__file__).parent / "contador1.txt"

def leer_contador(nombre_archivo: Path):
    # Si no existe, lo creamos con valor inicial
    if not nombre_archivo.exists():
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("0; 3.0\n")  # contador; pi

    # Leemos la última línea del archivo
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    if not lineas:
        # Por si el archivo está vacío
        return 3.0, 2, 0  # pi, n, contador

    ultima = lineas[-1].strip()
    try:
        contador_str, pi_str = ultima.split(";")
        contador = int(contador_str.strip())
        pi = float(pi_str.strip())
        n = 2 + 2 * contador  # Calculamos n según el contador
        return pi, n, contador
    except Exception:
        # Si hay algún error en el archivo, reiniciamos
        return 3.0, 2, 0

def aproximacion(pi, n, contador):
    while True:
        print(f"Iteración {contador} --> π ≈ {pi}")
        usuarioIntroduce = input("Enter para siguiente iteración o 's' para salir: ").strip().lower()
        
        if usuarioIntroduce == "s":
            break

        termino = 4 / (n * (n + 1) * (n + 2))
        if contador % 2 == 0:
            pi += termino
        else:
            pi -= termino

        n += 2
        contador += 1

        # Guardamos cada iteración
        with open(nombre_archivo, "a", encoding="utf-8") as f:
            f.write(f"{contador}; {pi}\n")

# Lectura inicial
pi, n, contador = leer_contador(nombre_archivo)
aproximacion(pi, n, contador)