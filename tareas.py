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