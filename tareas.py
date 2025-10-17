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
    
    