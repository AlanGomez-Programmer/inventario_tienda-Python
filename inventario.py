from utilidades import mostar_separadores, pedir_num_enteros

def menu():
    mostar_separadores()
    print("--- MENU DE INVENTARIO ---")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Actualizar Cantidad")
    print("4. Eliminar Producto")
    print("5. Calcular Valor Total del Inventario")
    opci = pedir_num_enteros("Ingrese una opción: ")
