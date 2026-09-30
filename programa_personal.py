# Registro de Observacion Astronomica - Version 4.0

MINUTOS_POR_HORA = 60


# Version 3.0: convertir los minutos a horas
def calcular_horas(minutos):
    horas = minutos / MINUTOS_POR_HORA
    return round(horas, 2)


# Version 3.0: clasificar la duracion de la observacion
def clasificar_observacion(minutos):
    if minutos >= 60:
        return "Observacion larga"
    elif minutos >= 30:
        return "Observacion moderada"
    else:
        return "Observacion corta"


# Version 3.0: mostrar el resumen de la observacion
def mostrar_resumen(nombre, objeto, minutos, horas, tipo_observacion):
    print("\n--- Registro de Observacion ---")
    print("Usuario:", nombre)
    print("Objeto observado:", objeto)
    print("Tiempo en minutos:", minutos)
    print("Tiempo en horas:", horas)
    print("Tipo de observacion:", tipo_observacion)


# Version 4.0: arreglo unidimensional con cinco objetos
objetos = ["Luna", "Marte", "Jupiter", "Venus", "Mercurio"]
print("Objetos disponibles:", objetos)

# Acceder a los cinco elementos mediante sus indices
print("Primer objeto:", objetos[0])
print("Segundo objeto:", objetos[1])
print("Tercer objeto:", objetos[2])
print("Cuarto objeto:", objetos[3])
print("Quinto objeto:", objetos[4])

# Version 4.0: modificar un elemento existente
objetos[4] = "Saturno"
print("Catalogo actualizado:", objetos)

# Version 4.0: recorrer el arreglo
for objeto_disponible in objetos:
    print(objeto_disponible)

# Version 4.0: almacenar las observaciones ingresadas
observaciones = []
continuar = "s"

while continuar == "s":
    nombre = input("\nNombre del usuario: ")
    objeto = input("Objeto astronomico observado: ").strip()

    # Version 4.0: verificar que el nombre del objeto tenga caracteres
    while objeto == "":
        objeto = input("Escribe el nombre del objeto: ").strip()

    # Version 4.0: validar los minutos ingresados
    while True:
        try:
            minutos = int(input("Minutos de observacion: "))
            if minutos > 0:
                break
            print("Escribe una cantidad mayor que cero.")
        except ValueError:
            print("Escribe los minutos como un numero entero.")

    # Conservar las funciones de la version anterior
    horas = calcular_horas(minutos)
    tipo_observacion = clasificar_observacion(minutos)

    mostrar_resumen(
        nombre,
        objeto,
        minutos,
        horas,
        tipo_observacion
    )

    # Version 4.0: longitud y acceso mediante indice
    print("\nCantidad de caracteres:", len(objeto))
    print("Primer caracter:", objeto[0])

    # Version 4.0: recorrer los caracteres
    print("Caracteres del nombre:")
    for caracter in objeto:
        print(caracter)

    # Version 4.0: buscar texto y convertir a mayusculas
    print("Contiene la palabra luna:", "luna" in objeto.lower())
    print("Nombre en mayusculas:", objeto.upper())

    # Version 4.0: añadir una fila con tres datos
    observaciones.append([objeto, minutos, horas])

    # Version 4.0: completar las dos filas requeridas
    if len(observaciones) < 2:
        print("\nRegistra otra observacion para completar las dos filas.")
    else:
        continuar = input(
            "\nDesea registrar otra observacion? (s/n): "
        ).strip().lower()

# Version 4.0: consultar un dato mediante dos indices
print("\nObjeto de la primera fila:", observaciones[0][0])

# Version 4.0: recorrer la estructura mostrando una fila por observacion
print("\nTabla de observaciones")
print("Objeto Minutos Horas")

for fila in observaciones:
    for dato in fila:
        print(dato, end=" ")
    print()