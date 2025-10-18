import json
import os

ARCHIVO = "tareas.json"

def cargar_tareas():
    """Carga las tareas desde el archivo."""
    if os.path.exists(ARCHIVO):
        try:
            with open(Archivo, 'r') as f:
                return json.load(f)
        except:
            return []
        return []
    
def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea(tareas):
    """Agrega una nueva tarea."""
    descripcion = input("\nDescripción: ").strip()
    if descripcion:
        tarea = {
            "id": len(tareas) + 1,
            "descripcion": descripcion,
            "completada": False
        }    
        tareas.append(tarea)
        guardar_tareas(tareas)
        print("¡Tarea agregada!")
    else:
        print("La descripción no puede estar vacía.")

def listar_tareas(tareas):
    """Lista todas las tareas."""
    if not tareas:
        print("\nNo hay tareas.")
        return
    
    print("\n--- TAREAS ---")
    for t in tareas:
        estado = "Completada" if t["completada"] else "Pendiente"
        print(f"{t['id']}. [{estado}] {t['description']}")

def marcar_completada(tareas):
    """Marca una tarea como completada."""
    if not tareas:
        print("\nNo hay tareas.")
        return
    
    listar_tareas(tareas)
    try:
        id_tarea = int(input("\nID de la tarea: "))
        for t in tareas:
            if t["id"] == id_tarea:
                t["completada"] = True
                guardar_tareas(tareas)
                print("¡Tarea completada!")
                return
            print("ID no encontrado.")
    except:
        print("ID inválido.")

def eliminar_tarea(tareas):
    """Elimina una tarea."""
    if not tareas:
        print("\nNo hay tareas.")
        return
    
    listar_tareas(tareas)
    try:
        id_tarea = int(input("\nID de la tarea a eliminar: "))
        for i, t in enumerate(tareas):
            if t["id"] == id_tarea:
                tareas.pop(i)

                for j, tarea in enumerate(tareas):
                    tarea["id"] = j +1
                guardar_tareas(tareas)
                print("¡Tarea eliminada!")
                return
        print("ID no encontrado.")
    except:
        print("ID inválido")

