from datetime import datetime
from Periodico import Periodico
from Digital import Digital
from Papel import Papel

if __name__ == "__main__":
    periodico1 = Periodico("La Nación", "Gobierno anuncia nuevas medidas económicas", "Carlos Martínez", datetime(2023, 2, 1))
    periodico2 = Periodico("El País Actual", "Expertos alertan sobre cambio climático", "Lucía Fernández", datetime(2023, 7, 12))

    periodico_digital1 = Digital("Noticias Hoy", "Innovación tecnológica acelera la industria", "Antonio Tete", datetime(2021, 11, 15), "www.noticiashoy.com", 560, 8, 10.0)
    periodico_digital2 = Digital("Mundo Digital", "Avances en inteligencia artificial este año", "Laura Gómez", datetime(2022, 2, 2), "www.mundodigital.com", 430, 1, 24.0)

    periodico_papel1 = Papel("Diario Económico", "Mercados internacionales muestran crecimiento", "Ana Teclado", datetime(2023, 12, 2), 4, "Alta", 4000, 2, True, 1000)
    periodico_papel2 = Papel("El Observador", "Crisis energética preocupa a Europa", "Jorge García", datetime(2026, 1, 3), 12, "Media", 6450, 3.50, False, 4000)
   
    lista_papeles = [periodico_papel1, periodico_papel2]
    lista_digitales = [periodico_digital1, periodico_digital2]

    while True:
        print("Menú periodicos")
        print("1. Listar periodicos en papel.")
        print("2. Listar periodicos digitales.")
        print("3. Añadir periodico en papel.")
        print("4. Añadir periodico digital.")
        print("5. Salir")

        opcionMenu = int(input("Selecione una opción: "))

        if opcionMenu == 1:
            print("Periodicos en papel")
            for p in lista_papeles:
                print(p)
            input()
        
        elif opcionMenu == 2:
            print("Periodicos digitales")
            for p in lista_digitales:
                print(p)
            input()
        
        elif opcionMenu == 3:
            print("Añade un periodico de papel: ")
            nombre_papel = input("Introduce el nombre del periódico: ")
            titular_papel = input("Introduce el titular: ")
            autor_papel = input("Introduce su autor: ")
            fecha_salida_papel = datetime.strptime(input("Introduce la fecha de salida(YYYY-MM-DD): "), "%Y-%m-%d")
            num_edicion = int(input("Introduce el número de la edición: "))
            while num_edicion < 0:
                num_edicion = int(input("Cantidad no válida. Introduce el número de la edición: "))
    
            calidad_papel = input("Introduce la calidad ('Alta', 'Media', 'Baja'): ")
            cantidad_papel = int(input("Introduce la cantidad de ejemplares a vender: "))
           
            while cantidad_papel < 0:
                cantidad_papel = int(input("Cantidad no válida. Introduce la cantidad de ejemplares a vender: "))
            
            precio_papel = float(input("Introduce el precio del periódico: "))
            
            while precio_papel < 0:
                precio_papel = float(input("Precio no válido. Ingresa una cantidad realista: "))
            precio_papel = round(precio_papel, 2)
            
            fasciculos = input("Incluye fascículos (S/N): ").upper()
            if fasciculos == "S":
                fasciculos = True
            else:
                fasciculos = False
            vendidos = 0
            
            nuevo_papel = Papel(nombre_papel, titular_papel, autor_papel, fecha_salida_papel, num_edicion, calidad_papel, cantidad_papel, precio_papel, fasciculos, vendidos)
            lista_papeles.append(nuevo_papel)
            input()
        
        elif opcionMenu == 4:
            print("Añade un periodico digital: ")
            nombre_digital = input("Introduce el nombre del periódico: ")
            titular_digital = input("Introduce el titular: ")
            autor_digital = input("Introduce su autor: ")
            fecha_salida_digital = datetime.strptime(input("Introduce la fecha de salida(YYYY-MM-DD): "), "%Y-%m-%d")
            dominio = input("Dominio web: ")
            num_visitas = 0
            suscriptores = 0
            precio_suscripcion = float(input("Introduce precio de la suscripción: "))
           
            while precio_suscripcion < 0:
                precio_suscripcion = float(input("Precio no válido. Ingresa una cantidad realista: "))
            precio_suscripcion = round(precio_suscripcion, 2)
            

            nuevo_digital = Digital(nombre_digital, titular_digital, autor_digital, fecha_salida_digital, dominio, num_visitas, suscriptores, precio_suscripcion)
            lista_digitales.append(nuevo_digital)
            input()

        elif opcionMenu == 5:
            break

