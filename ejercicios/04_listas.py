
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
    
tickets = ["error al cargar el sistema", "lento el window", "crash", "mal funcionamiento", "no puedo ingresar", "urgente", "impresora", "error 500"]
print("Número de tickets:", len(tickets))
print("Tickets:", tickets[0])
print("Tickets:", tickets[7])
tickets.append("caído el servidor")
print("Número de tickets:", len(tickets))

print("--------------------------------------------")

for ticket in tickets:
    prioridad, mensaje = asignar_prioridad(ticket)
    print(f"Ticket: {ticket}, Prioridad: {prioridad}, Mensaje: {mensaje}")

print("--------------------------------------------")

criticos = 0
altos = 0
medios = 0
bajos = 0
for ticket in tickets:
    prioridad, mensaje = asignar_prioridad(ticket)
    if prioridad == 4:
        criticos += 1
    elif prioridad == 3:
        altos += 1
    elif prioridad == 2:
        medios += 1
    else:
        bajos += 1

print(f"Total de tickets procesados: {len(tickets)}")
print(f"Tickets críticos: {criticos}, Tickets altos: {altos}, Tickets medios: {medios}, Tickets bajos: {bajos}")