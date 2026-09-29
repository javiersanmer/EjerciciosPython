from pathlib import Path

ruta = Path(__file__).parent / "tablas_multiplicar.txt"

with open(ruta, "w", encoding="utf-8") as f:
    for t in range(0,11):
        f.write(f"Tabla del {t}: \n")
        for i in range(0,11):
            f.write(f"{t} x {i} = {t*i}\n")
        f.write(f"\n")  