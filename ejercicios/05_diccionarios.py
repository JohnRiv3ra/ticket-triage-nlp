#03_funciones.py
def asignar_prioridad(descripcion):
    descripcion = descripcion.lower()
    
    # Todo el bloque de condiciones debe estar indentado dentro de la función
    if "urgente" in descripcion or "caido" in descripcion or "caído" in descripcion:
        prioridad = 4
        return prioridad, "Prioridad crítica: atender de inmediato"
    elif "error" in descripcion:
        prioridad = 3
        return prioridad, "Prioridad alta: atender en las próximas horas"
    elif "no puedo" in descripcion or "lento" in descripcion:
        prioridad = 2
        return prioridad, "Prioridad media: atender en el plazo establecido"
    else:
        prioridad = 1
        return prioridad, "Prioridad baja: atender cuando haya tiempo"

print("--------------------------------------------")

# Diccionarios tickets
tickets = [

    {"id": 1, "descripcion": "El servidor está caído", "prioridad": None},
    {"id": 2, "descripcion": "La impresora no funciona", "prioridad": None},
    {"id": 3, "descripcion": "No puedo ingresar al ERP, sale error 500", "prioridad": None},
    {"id": 4, "descripcion": "El sistema está lento", "prioridad": None},
    {"id": 5, "descripcion": "Error al cargar el sistema", "prioridad": None}
]
print(tickets)

for ticket in tickets:
    prioridad, mensaje = asignar_prioridad(ticket["descripcion"])
    ticket["prioridad"] = prioridad
    print(f"Ticket {ticket['id']}: {mensaje}")
print(tickets)

print("--------------------------------------------")

ticket_ejemplo= {
    "id": 1,
    "categoria": "Sistemas",
    "descripcion": "No puedo iniciar sesión en la aplicación",
    "prioridad": 3
}
print("Descripción:", ticket_ejemplo["descripcion"])
print(f"Ticket: {ticket_ejemplo['id']}, Categoría: {ticket_ejemplo['categoria']}, Prioridad: {ticket_ejemplo['prioridad']}")
ticket_ejemplo["descripcion"] = "Error al cargar el sistema"
ticket_ejemplo["status"] = False
print(ticket_ejemplo)
print(type(ticket_ejemplo["prioridad"]))
print(ticket_ejemplo["prioridad"] == 3)

