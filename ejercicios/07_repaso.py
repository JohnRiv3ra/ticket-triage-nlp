#importamos la función asignar_prioridad del módulo clasificador
import json
from clasificador import asignar_prioridad

# 1. Cargar los tickets desde tickets.json           → sesión 6
#    (guárdalos en una variable llamada tickets)

with open("tickets.json", "r", encoding="utf-8") as f:
    tickets = json.load(f)

# 2. Crear 4 contadores en 0                          → sesión 4

contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0

# 3. Recorrer los tickets con for:                    → sesiones 4 y 5
#    - clasificar la descripción de cada ticket
#    - guardar el número en ticket["prioridad"]
#    - sumar 1 al contador que corresponda

for ticket in tickets:
    print(ticket["descripcion"])
    prioridad = asignar_prioridad(ticket["descripcion"])[0]
    ticket["prioridad"] = prioridad
    if prioridad == 1:
        contador_1 += 1
    elif prioridad == 2:
        contador_2 += 1
    elif prioridad == 3:
        contador_3 += 1
    elif prioridad == 4:
        contador_4 += 1

# 4. Guardar la lista clasificada en un archivo NUEVO → sesión 6
#    llamado tickets_clasificados.json

with open("tickets_clasificados.json", "w", encoding="utf-8") as f:
    json.dump(tickets, f, ensure_ascii=False, indent=4)

# 5. Mostrar un resumen:                              → sesión 1 (f-strings)
#    total de tickets y cuántos hay de cada prioridad


print(f"Total de tickets: {len(tickets)}")
print(f"Tickets de prioridad 1: {contador_1}")
print(f"Tickets de prioridad 2: {contador_2}")
print(f"Tickets de prioridad 3: {contador_3}")
print(f"Tickets de prioridad 4: {contador_4}")



""" input_descripcion = input("Ingrese la descripción del ticket: ")
prioridad, mensaje = asignar_prioridad(input_descripcion)
print(f"Número de prioridad: {prioridad}, mensaje: {mensaje}") """