"""
Sistema de Gestión de Pedidos - AgroVerde
"""

# DATOS INICIALES
productos_disponibles = ["Tomates", "Lechugas", "Zanahorias", "Brócoli", "Espinacas"]

categorias = {"Verduras", "Hortalizas", "Tubérculos"}

pedidos = {
    "P001": {
        "cliente": ("Juan Pérez", "8888-8888", "San José"), "productos": ["Tomates", "Lechugas"], "estado": "Pendiente"
    }
}

contador_pedidos = 2

# FUNCIONES
def mostrar_menu():
    print("\n=== AGROVERDE ===")
    print("1. Ver productos")
    print("3. Eliminar producto")
    print("4. Crear pedidos")
    print("5. Ver pedidos")
    print("6. Estadísticas")
    print("0. Salir")

def ver_productos():
    print("\n--- PRODUCTOS ---")
    for i, prod in enumerate(productos_disponibles, 1):
        print(f"{i}. {prod}")
    print(f"Total: {len(productos_disponibles)}")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    if nombre:
        productos_disponibles.append(nombre)
        print("Producto agregado")

