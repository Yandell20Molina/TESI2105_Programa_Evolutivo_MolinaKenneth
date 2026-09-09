# Registro de Observacion Astronomica - Version 3.0

MINUTOS_POR_HORA = 60


# Nuevo en Version 3.0:
# Funcion para convertir los minutos de observacion a horas
def calcular_horas(minutos):
    horas = minutos / MINUTOS_POR_HORA
    return round(horas, 2)


# Nuevo en Version 3.0:
# Funcion para clasificar la duracion de la observacion
def clasificar_observacion(minutos):

    # Nueva decision para clasificar la duracion de la observacion
    if minutos >= 60:
        tipo_observacion = "Observacion larga"

    elif minutos >= 30:
        tipo_observacion = "Observacion moderada"

    else:
        tipo_observacion = "Observacion corta"

    return tipo_observacion


# Nuevo en Version 3.0:
# Funcion para mostrar el resumen de la observacion
def mostrar_resumen(nombre, objeto, minutos, horas, tipo_observacion):
    print("\n--- Registro de Observacion ---")
    print("Usuario:", nombre)
    print("Objeto observado:", objeto)
    print("Tiempo en minutos:", minutos)
    print("Tiempo en horas:", horas)
    print("Tipo de observacion:", tipo_observacion)


# Nueva variable para controlar la repeticion del programa
continuar = "s"


# Nuevo ciclo para permitir registrar mas de una observacion
while continuar == "s":

    nombre = input("Nombre del usuario: ")
    objeto = input("Objeto astronomico observado: ")
    minutos = int(input("Minutos de observacion: "))

    # Nuevo en Version 3.0:
    # Se llaman las funciones para procesar los datos
    horas = calcular_horas(minutos)
    tipo_observacion = clasificar_observacion(minutos)

    mostrar_resumen(
        nombre,
        objeto,
        minutos,
        horas,
        tipo_observacion
    )

    # Nueva entrada para decidir si se repite el registro
    continuar = input(
        "\nDesea registrar otra observacion? (s/n): "
    ).lower()