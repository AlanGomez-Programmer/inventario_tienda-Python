from utilidades import ( 
    mostar_separadores, 
    pedir_num_enteros, 
    ruta_inventario, 
    leer_archivo, 
    guardar_datos,
    validar_producto, 
    pedir_precio, 
    pedir_cantidad
) 

def menu():
    while True:
        mostar_separadores()
        print("--- MENU DE INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Actualizar Cantidad")
        print("4. Eliminar Producto")
        print("5. Calcular Valor Total del Inventario")
        opci = pedir_num_enteros("Ingrese una opción: ")

        if opci == 1:
            agregar_producto()

def agregar_producto():
    productos = leer_archivo(ruta_inventario)
    mostar_separadores()
    print("--- REGISTRO DE PRODUCTO ---")
    nombre_producto = validar_producto()
    precio = pedir_precio()
    cantidad = pedir_cantidad()

    producto = {
        "precio": precio,
        "cantidad": cantidad
    }
    
    productos[nombre_producto] = producto

    guardar_datos(ruta_inventario, productos)
    print(f"\033[033Producto Registrado exitosamente \033[0m")
