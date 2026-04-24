from utilidades import ( 
    mostar_separadores, 
    pedir_num_enteros, 
    ruta_inventario, 
    leer_archivo, 
    guardar_datos,
    validar_producto, 
    pedir_precio, 
    pedir_cantidad,
    producto_existe
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

def listar_productos():
    productos = leer_archivo(ruta_inventario)

    if len(productos) == 0:
        print(f"\033[031mERROR: No hay productos por mostrar \033[0m")
        return
    else:
        contador = 0
        for producto in productos:
            precio = productos[producto]["precio"]
            cantidad = productos[producto]["cantidad"]
            contador += 1
            print("-"*40)
            print(f"{contador}. {producto}")
            print(f"PRECIO: {precio}")
            print(f"CANTIDAD DE PRODUCTOS DISPONIBLES: {cantidad}")

def actualizar_cantidad():
    productos = leer_archivo(ruta_inventario)
    mostar_separadores()
    print("--- ACTULIZACION DE CANTIDAD DE PRODUCTOS ---")
    producto = producto_existe()
    cantidad = pedir_cantidad()

    if producto in productos:
        productos[producto]["cantidad"] = cantidad

    guardar_datos(ruta_inventario, productos)
    print(f"\033[033mCambio de cantidad de productos actualizado correctamente\033[0m")

def eliminar_producto():
    productos = leer_archivo(ruta_inventario)
    mostar_separadores()
    print("--- ELIMINAR UN PRODUCTO ---")
    
    producto = producto_existe()

    if producto in productos:
        productos.pop(producto)

    guardar_datos(ruta_inventario, productos)

def calcular_valor_total():
    productos = leer_archivo(ruta_inventario)

    mostar_separadores()
    print("--- VALOR TOTAL DEL INVENTARIO ---")

    if len(productos) == 0:
        print(f"\033[031mERROR: No hay productos agregados \033[0m")
        return

    operacion = 0
    total = 0

    for  producto in productos:
        precio = productos[producto]["precio"]
        cantidad = productos[producto]["cantidad"]
        operacion = precio * cantidad
        total += operacion 

    print(f"El valor total del inventario es: {total}")   