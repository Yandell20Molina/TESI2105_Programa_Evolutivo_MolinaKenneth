# Registro de Observacion Astronomica - Version 2.0

MINUTOS_POR_HORA = 60

# Nueva variable para controlar la repeticion del programa
continuar = "s"

# Nuevo ciclo para permitir registrar mas de una observacion
while continuar == "s":
    nombre = input("Nombre del usuario: ")
    objeto = input("Objeto astronomico observado: ")
    minutos = int(input("Minutos de observacion: "))

    horas = minutos / MINUTOS_POR_HORA

    # Nueva decision para clasificar la duracion de la observacion
    if minutos >= 60:
        tipo_observacion = "Observacion larga"
    elif minutos >= 30:
        tipo_observacion = "Observacion moderada"
    else:
        tipo_observacion = "Observacion corta"

    print("\n--- Registro de Observacion ---")
    print("Usuario:", nombre)
    print("Objeto observado:", objeto)
    print("Tiempo en minutos:", minutos)
    print("Tiempo en horas:", horas)
    print("Tipo de observacion:", tipo_observacion)

    # Nueva entrada para decidir si se repite el registro
    continuar = input("\nDesea registrar otra observacion? (s/n): ")
    