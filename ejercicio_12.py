#Diseñar un algoritmo para validar una fecha en el formato dd/mm/aaaa. Se considera que una fecha es válida si está entre 01/01/1900 y 31/12/2100, el mes entre 1 y 12 y el día entre 1 y 31, teniendo en cuenta que algunos meses tienen 28 (o 29), 30 o 31 días. Si la fecha no es válida se muestra un mensaje de error y se vuelve a leer los datos. El algoritmo termina cuando la fecha ingresada es válida.


def validar_fecha():
    while True:
        fecha_str = input("Ingrese la fecha en formato dd/mm/aaaa: ")
        try:
            dia_str, mes_str, año_str = fecha_str.split('/')
            dia = int(dia_str)
            mes = int(mes_str)
            año = int(año_str)

            if not (1900 <= año <= 2100):
                print("Error: Año fuera del rango permitido (1900-2100).")
                continue

            if not (1 <= mes <= 12):
                print("Error: Mes inválido (debe estar entre 1 y 12).")
                continue

            if mes in [1, 3, 5, 7, 8, 10, 12]:
                dias_mes = 31
            elif mes in [4, 6, 9, 11]:
                dias_mes = 30
            elif mes == 2:
                es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
                if es_bisiesto:
                    dias_mes = 29
                else:
                    dias_mes = 28
            else:
                # Ya validamos el mes antes, esta rama no debería alcanzarse
                dias_mes = 0 # Valor no válido para forzar error si algo sale mal

            if not (1 <= dia <= dias_mes):
                print(f"Error: Día inválido para el mes {mes} de {año}. Debe estar entre 1 y {dias_mes}.")
                continue

            # Si llegamos aquí, la fecha es válida
            print("Fecha válida.")
            break

        except ValueError:
            print("Error: Formato de fecha incorrecto. Use dd/mm/aaaa.")

# Iniciar la validación de fecha
validar_fecha()