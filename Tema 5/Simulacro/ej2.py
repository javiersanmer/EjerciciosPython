from datetime import datetime, timedelta,date
from datos import get_mantecados
from ej1 import Mantecado
class Almacen:
    def __init__(self, id: int, direccion: str, mantecados: list[Mantecado] | None = None) -> None:
        self.id = id
        self.direccion = direccion
        if mantecados is None:
            self.mantecados = []
        else:
            self.mantecados = mantecados
    def total_mantecados(self) -> int: #cae
        return len(self.mantecados)
    
    def aniadir_mantecado(self, m: Mantecado) -> None: #cae
        self.mantecados.append(m)
    
    def eliminar_mantecado(self, m: Mantecado) -> None: #cae
        for m in self.mantecados:
            if m.id == id:
                self.mantecados.remove(m)
                return True
            return False

    def mantecados_caducados(self, m: Mantecado) -> list[Mantecado]:
        return [m for m in self.mantecados if m.esta_caducado()]
    
    def proximos_a_caducar(self, n:int) -> list[Mantecado]:
        hoy = date.today()
        return [m for m in self.mantecados if 0 <= (m.fecha_caducidad - hoy).days <= n]
        #return [m for m in self.mantecados if 0 <= m.dias_para_caducar() <= n]

    def mantecados_en_rango_precio(self, minimo:float, maximo:float) -> list[Mantecado]:
        resultado = []
        for mantecado in self.mantecados:
            if mantecado.precio > minimo and mantecado.precio < maximo:
                resultado.append(mantecado)
            return resultado
    #return [m for m in self.mantecados if minimo <= m.precio <= maximo]
    
    def sin_ingredientes(self, ingrediente: str) -> list[Mantecado]: #cae, dime las mascotass q tienen la rabia
        return [m for m in self.mantecados if ingrediente not in m.ingredientes]
        
    def reporte_por_ingrediente(self) -> dict[str, int]:
        reporte = {}
        for m in self.mantecados:
            for ing in m.ingredientes:
                reporte[ing] = reporte.get(ing, 0) + 1
        return reporte

    def reporte_por_tipo(self) -> dict[str, int]:
        reporte = {}
        for m in self.mantecados:
            reporte[m.tipo] = reporte.get(m.tipo, 0) + 1
        return reporte
    
if __name__ == "__main__":
    from datos import get_mantecados
    from datetime import date, timedelta

    lista = get_mantecados(0)#se pone 0 pq accede al dataset 0, EN EL EXAMEN ES SIN 0
    hoy = datetime.today()
    almacen = Almacen(1, "Calle nse", lista)

    print("=== ESTADO INICIAL ===")
    print(f"Total mantecados: {almacen.total_mantecados()}")

    for m in almacen.mantecados:
        if m.id == 3:
            almacen.eliminar_mantecado(m)
            print(f"Eliminado")
            break
    
    print(f"Total tras eliminar: {len(almacen.mantecados)}")

    resultado = almacen.mantecados_caducados(hoy)
    print("=== CADUCADOS ===")
    for mantecado in resultado:
        print(f"{mantecado.id} {mantecado.tipo}")

    resultado = almacen.proximos_a_caducar(3)
    print("=== PRÓXIMOS A CADUCAR (<= 3 días) ===")
    for mantecado in resultado:
        print(f"{mantecado.id} {mantecado.tipo}")

    resultado = almacen.mantecados_en_rango_precio(2.0, 3.0)
    print("=== RANGO DE PRECIO (2.0 - 3.0)")
    for mantecado in resultado:
        print(f"{mantecado.id} {mantecado.tipo} {mantecado.precio}")

    print("=== SIN AZÚCAR ===")
    for m in almacen.mantecados:
        pass

    print("===== REPORTE POR INGREDIENTE =====")
    for ing, cantidad in almacen.reporte_por_ingrediente().items():
        print(ing, "->", cantidad)
    print()


    print("===== REPORTE POR TIPO =====")
    for tipo, cantidad in almacen.reporte_por_tipo().items():
        print(tipo, "->", cantidad)