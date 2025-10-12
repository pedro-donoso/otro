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

    sistema["citas"].append(cita)
    print(f"Cita agendada para {mascota['nombre']} el {fecha} a las {hora}")
    return True

def registrar_tratamiento(sistema, id_mascota, fecha, diagnostico, medicamentos):
    """
    Registra un tratamiento para una mascota.
    Retorna True si se registró correctamente.
    """
    if id_mascota not in sistema["mascotas"]:
        print(f"Error: No existe mascota con ID {id_mascota}")
        return False
    
    tratamiento = {
        "id": len(sistema["tratamientos"]) + 1,
        "id_mascota": id_mascota,
        "fecha": fecha,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }

    sistema["tratamientos"].append(tratamiento)
    sistema["mascotas"][id_mascota]["historial"].append(tratamiento["id"])

    print(f"Tratamiento registrado")
    return True

def mostrar_citas_del_dia(sistema, fecha):
    """Muestra todas las citas de una fecha específica."""
    citas_del_dia = [c for c in sistema["citas"] if c["fecha"] == fecha]

    if not citas_del_dia:
        print(f"No hay citas para el {fecha}")
        return
    
    print(f"\n--- CITAS DEL {fecha} ---")
    for cita in sorted(citas_del_dia, key=lambda x: x["hora"]):
        print(f"{cita['hora']} - {cita['mascota']} (Dueño: {cita['dueno']}) - Dr. {cita['veterinario']}")

def mostrar_historial(sistema, id_mascota):
    """Muestra el historial médico de una mascota."""
    if id_mascota not in sistema["mascota"]:
        print(f"Error: No existe mascota con ID {id_mascota}")
        return
    
    mascota = sistema["mascotas"][id_mascota]
    print(f"\n---HISTORIAL DE {mascota['nombre'].upper()} ---")
    print(f"Tipo: {mascota['tipo']}")
    print(f"Dueño: {mascota['dueno']}")

    if not mascota["historial"]:
        print("Sin tratamientos registrados")
        return

    print("\nTratamientos:")
    for id_trat in mascota["historial"]:
        trat = next(t for t in sistema["tratamientos"] if t["id"] == id_trat)
        print(f" . {trat['fecha']}: {trat['diagnostico']}")
        print(f" Medicamentos: {', '.join(trat['medicamentos'])}")

def horarios_disponibles(sistema, fecha):
    """
    Retorna lista de horarios disponibles para una fecha.
    """
    todos_horarios = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"]
    disponibles = []

    for hora in todos_horarios:
        if verificar_disponibilidad(sistema, fecha, hora):
            disponibles.append(hora)

    return disponibles

def main():
    print("\n=== SISTEMA VETCARE ===\n")

    sistema = crear_sistema()

    print("--- Registrando Mascotas ---")
    id1 = registrar_mascota(sistema, "Max", "Perro", "Carlos Pérez", "555-0101")
    id2 = registrar_mascota(sistema, "Luna", "Gato", "María González", "555-0102")
    id3 = registrar_mascota(sistema, "Rocky", "Perro", "Juan Rodríguez", "555-0103")

    print("\n--- Agendando Citas ---")
    agendar_cita(sistema, id1, "15/10/2025", "10:00", "Dr. Martínez")
    agendar_cita(sistema, id2, "15/10/2025", "11:00", "Dra. López")
    agendar_cita(sistema, id3, "15/10/2025", "10:00", "Dr. Martínez")
    agendar_cita(sistema, id3, "15/10/2025", "14:00", "Dr.Martínez")

    print("\n--- Horarios Disponibles 15/10/2025 ---")
    disponibles = horarios_disponibles(sistema, "15/10/2025")
    print(f"Horarios libres: {', '.join(disponibles)}")

    mostrar_citas_del_dia(sistema, "15/10/2025")

    

