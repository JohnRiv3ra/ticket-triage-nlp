#CONDICIONALES PRIORIDAD DE TICKETS
prioridad = 3
if prioridad == 4:
    print("Prioridad crítica: atender de inmediato")
elif prioridad == 3:
    print("Prioridad alta: atender en las próximas horas")
elif prioridad == 2:
    print("Prioridad media: atender en el plazo establecido")
else:
    print("Prioridad baja: atender cuando haya tiempo")

prioridad = 7
if prioridad == 4:
    print("Prioridad crítica: atender de inmediato")
elif prioridad == 3:
    print("Prioridad alta: atender en las próximas horas")
elif prioridad == 2:
    print("Prioridad media: atender en el plazo establecido")
elif prioridad == 1:
    print("Prioridad baja: atender cuando haya tiempo") 
else:
    print("Prioridad desconocida: revisar el valor de la variable")

print("----------------------------------------")

#CONDICIONALES DESCRIPCION DE TICKETS
descripcion = "No puedo ingresar al ERP, sale error 500"
if "ERP" in descripcion:
    print("Ticket relacionado con el ERP")
else:
    print("Ticket no relacionado con el ERP")

print("----------------------------------------")

#CONDICIONALES DESCRIPCION DE TICKETS (MAYUSCULAS Y MINUSCULAS)
descripcion = "URGENTE: El servidor está caído, no puedo acceder a la base de datos"
descripcion = descripcion.lower()
if "urgente" in descripcion or "caido" in descripcion or "caído" in descripcion:
    prioridad = 4
    print("Prioridad crítica: atender de inmediato")
elif "error" in descripcion:
    prioridad = 3
    print("Prioridad alta: atender en las próximas horas") 
elif "no puedo" in descripcion or "lenta" in descripcion:
    prioridad = 2
    print("Prioridad media: atender en el plazo establecido")
else:
    prioridad = 1
    print("Prioridad baja: atender cuando haya tiempo")