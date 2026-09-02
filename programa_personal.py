MINUTOS_POR_HORA = 60

nombre = input("Nombre del usuario: ")
objeto = input("Objeto astronomico observado: ")
minutos = int(input("Minutos de observacion: "))

horas = minutos / MINUTOS_POR_HORA

print("\n--- Registro de Observacion ---")
print("Usuario:", nombre)
print("Objeto observado:", objeto)
print("Tiempo en minutos:", minutos)
print("Tiempo en horas:", horas)
