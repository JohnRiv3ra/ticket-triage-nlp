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

numero, mensaje = asignar_prioridad("El servidor está caído")
print(f"Número de prioridad: {numero}, Mensaje: {mensaje}")

numero, mensaje = asignar_prioridad("No puedo ingresar al ERP, sale error 500")
print(f"Número de prioridad: {numero}, Mensaje: {mensaje}")

numero, mensaje = asignar_prioridad("El sistema está lento")
print(f"Número de prioridad: {numero}, Mensaje: {mensaje}")