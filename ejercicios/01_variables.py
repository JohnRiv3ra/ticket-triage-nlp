# Una variable es una "caja" con nombre donde guardas un dato.
# Las líneas que empiezan con # son comentarios: Python las ignora.

# --- Texto (str) ---
descripcion = "No puedo ingresar al ERP, sale error 500"
categoria = "Sistemas"

# --- Números enteros (int) ---
id_ticket = 1024
prioridad = 3          # 1 = Baja, 2 = Media, 3 = Alta, 4 = Crítica

# --- Números decimales (float) ---
horas_abierto = 2.5

# --- Verdadero/Falso (bool) ---
resuelto = False

# --- Mostrar datos en pantalla ---
print(descripcion)
print(id_ticket)

# type() te dice qué tipo de dato es una variable
print(type(descripcion))
print(type(id_ticket))
print(type(horas_abierto))
print(type(resuelto))

# --- f-strings: mezclar texto y variables ---
print(f"Ticket #{id_ticket} | Categoría: {categoria} | Prioridad: {prioridad}")
print(f"Lleva {horas_abierto} horas abierto. ¿Resuelto? {resuelto}")


# --- Reto: segundo ticket ---
descripcion2 = "No puedo imprimir desde la aplicación de contabilidad"
id_ticket2 = 1025
prioridad2 = 2
horas_abierto2 = 1.5
resuelto2 = True
categoria2 = "Hardware"

print(f"Ticket #{id_ticket2} | Categoría: {categoria2} | Prioridad: {prioridad2}")
print(f"Lleva {horas_abierto2} horas abierto. ¿Resuelto? {resuelto2}")

print("Ticket " + str(id_ticket))
print("Ticket " + str(id_ticket2))
