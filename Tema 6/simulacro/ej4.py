from ej2 import CuentaCorriente
from ej3 import CuentaAhorro

if __name__ == '__main__':
    cc1 = CuentaCorriente("Ana López", "ES001", 500.0, 300.0)
    cc2 = CuentaCorriente("Carlos Ruiz", "ES002", 100.0, 200.0)

    ca1 = CuentaAhorro("Marta Gómez", "ES003", 1000.0, 2.5)
    ca2= CuentaAhorro("Luis Torres", "ES004", 2500.0, 3.0)

    print("=== ESTADO INICIAL ===")
    print(cc1) #Si son 3 o más de una misma clase se hace con for en una lista
    print(cc2)
    print(ca1)
    print(ca2)
    print()

    print("=== INGRESOS (200€ para Ana y 500€ para Marta) ===")
    cc1.ingresar(200.0)
    print(cc1)
    ca1.ingresar(500.0)
    print(ca1)
    print()

    print("=== RETIRADAS (250€ para Carlos y 2000€ para Marta) ===")
    print(f"Retirada cc2 (250): {cc2.retirar(250)}")
    print(f"Retirada ca1 (2000): {ca1.retirar(2000)}")
    cc2.retirar(250)
    print(cc2)
    ca1.retirar(2000)
    print(ca1)
    print()

    print("=== INTERESES ===")
    ca2.aplicar_intereses()
    print(ca2)
    print()

    print("=== COBRO COMISION ===")
    cc1.cobrar_comision()
    ca1.cobrar_comision()
    print(cc1)
    print(ca1)
    print()

    print("=== COMPROBAR IGUALDAD Y HASH ===")
    print("Para == creamos una cuenta corriente con el mismo número que cc1 pero datos distintos")
    cc1_duplicada = CuentaCorriente("Ana NoLopez", "ES001", 400.0, 200.0)
    print(f"cc1 == cc1_duplicada: {cc1 == cc1_duplicada}")
    print("Creamos un set con ambas cuentas (debería haber solo una)")
    cuentas_set = {cc1, cc1_duplicada} #SI preguntan "Compruba q se funciona correctamente" lo podemos usar.
    print(f"Número de cuentas en set: {len(cuentas_set)}")
