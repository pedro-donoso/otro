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

