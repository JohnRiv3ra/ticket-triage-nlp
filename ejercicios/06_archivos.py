import json

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

tickets = [

    {"id": 1, "descripcion": "El servidor está caído", "prioridad": None},
    {"id": 2, "descripcion": "La impresora no funciona", "prioridad": None},
    {"id": 3, "descripcion": "No puedo ingresar al ERP, sale error 500", "prioridad": None},
    {"id": 4, "descripcion": "El sistema está lento", "prioridad": None},
    {"id": 5, "descripcion": "Error al cargar el sistema", "prioridad": None}
]


#archivos
# Escribir

with open("tickets.json", "w", encoding="utf-8") as archivo_json:
    json.dump(tickets, archivo_json, indent=4, ensure_ascii=False)

with open("tickets.json", "r", encoding="utf-8") as archivo_json:
    tickets_leidos = json.load(archivo_json)

for ticket in tickets_leidos:
    prioridad, mensaje = asignar_prioridad(ticket["descripcion"])
    ticket["prioridad"] = prioridad
    print(f"Ticket {ticket['id']}: {mensaje}")

with open("tickets.json", "w", encoding="utf-8") as archivo_json:
    json.dump(tickets_leidos, archivo_json, indent=4, ensure_ascii=False)
print("---------------------------------------------")

with open("tickets.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Descripción: El servidor está caído\n")
    archivo.write("Descripción: La impresora no funciona\n")

# Leer
with open("tickets.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)

