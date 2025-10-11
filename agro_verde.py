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

def eliminar_producto():
    ver_productos()
    try:
        num = int(input("Número a eliminar: ")) - 1
        if 0 <= num < len(productos_disponibles):
            productos_disponibles.pop(num)
            print("Producto eliminado")
    except:
        print("Error")

def crear_pedido():
    global contador_pedidos

    print("\n--- NUEVO PEDIDO ---")
    nombre = input("Nombre cliente: ")
    telefono = input("Teléfono: ")
    ubicacion = input("Ubicación: ")

    ver_productos()
    nums = input("Números de productos (separados por coma): ").split(",")

    productos_pedido = []
    for n in nums:
        try:
            i = int(n.strip()) - 1
            if 0 <= 1 < len(productos_disponibles):
                productos_pedido.append(productos_disponibles[i])
        except:
            pass

    if productos_pedido:
        id_pedido = f"P{contador_pedidos:03d}"
        contador_pedidos += 1

        pedidos[id_pedido] = {
            "cliente": (nombre, telefono, ubicacion),
            "productos": productos_pedido,
            "estado": "Pendiente"
        }
        print(f"Pedido {id_pedido} creado")

def ver_pedidos():
    print("\n--- PEDIDOS ---")
    for id_ped, info in pedidos.items():
        print(f"\n{id_ped}:")
        print(f" Cliente: {info['cliente'][0]}")
        print(f" Teléfono: {info['cliente'][1]}")
        print(f" Productos: {', '.join(info['productos'])}")
        print(f" Estado: {info['estado']}")

def estadisticas():
    print("\n--- ESTADÍSTICAS ---")
    print(f"Productos: {len(productos_disponibles)}")
    print(f"Categorías: {len(categorias)}")
    print(f"Pedidos: {len(pedidos)}")

    estados = {}
    for info in pedidos.values():
        estado = info["estado"]
        estados[estado] = estados.get(estado, 0) + 1

    print("\nPedidos por estado:")
    for estado, cant in estados.items():
        print(f" {estado}: {cant}")

