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

    