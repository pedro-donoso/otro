def crear_sistema():
    """Crea la estructura inicial del sistema."""
    return {
        "citas": [],
        "mascotas": {},
        "tratamientos": []
    }

def registrar_mascota(sistema, nombre, tipo, dueno, telefono):
    """
    Registra una nueva mascota.
    Retorna el ID de la mascota.
    """
    id_mascota = len(sistema["mascotas"]) + 1

    sistema["mascotas"][id_mascota] = {
        "id": id_mascota,
        "nombre": nombre,
        "tipo": tipo,
        "dueno": dueno,
        "telefono": telefono,
        "historial": []
    }

    print(f"Mascota '{nombre}' registrada con ID: {id_mascota}")
    return id_mascota

def verificar_disponibilidad(sistema, fecha, hora):
    """
    Verifica si un horario está disponible.
    Retorna True si está libre, False si está ocupado.
    """
    for cita in sistema["citas"]:
        if cita["fecha"] == fecha and cita["hora"] == hora:
            return False
        return True

def agendar_cita(sistema, id_mascota, fecha, hora, veterinario):
    """
    Agenda una cita para una mascota.
    Retorna True si se asignó, False si no.
    """

    if id_mascota not in sistema["mascotas"]:
        print(f"Error: No existe mascota con ID {id_mascota}")
        return False

    if not verificar_disponibilidad(sistema, fecha, hora):
        print(f"Error: El horario {fecha} {hora} ya está ocupado")
        return False
    
    mascota = sistema["mascotas"][id_mascota]
    cita = {
        "id": len(sistema["citas"]) + 1,
        "id_mascota": id_mascota,
        "mascota": mascota["nombre"],
        "dueno": mascota["dueno"],
        "fecha": fecha,
        "hora": hora,
        "veterinario": veterinario
    }

    