from utilidades import ( 
    mostrar_separadores, 
    pedir_num_enteros, 
    ruta_inventario, 
    leer_archivo, 
    guardar_datos,
    validar_producto, 
    pedir_precio, 
    pedir_cantidad,
    producto_existe,
    salida
) 

def menu():
    while True:
        mostrar_separadores()
        print("--- MENU DE INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Actualizar Cantidad")
        print("4. Eliminar Producto")
        print("5. Calcular Valor Total del Inventario")
        print("6. Salir")
        opci = pedir_num_enteros("Ingrese una opción: ")

        if opci == 1:
            agregar_producto()
        elif opci == 2:
            listar_productos()
        elif opci == 3:
            actualizar_cantidad()
        elif opci == 4:
            eliminar_producto()
        elif opci == 5:
            calcular_valor_total()
        elif opci == 6:
            print("Saliendo...")
            break
        else:
            print("\033[31mError: Opcion no existe \033[0m")
            salida()

def agregar_producto():
    productos = leer_archivo(ruta_inventario)
    mostrar_separadores()
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
    salida()

def listar_productos():
    productos = leer_archivo(ruta_inventario)
    mostrar_separadores()
    print("--- LISTADO DE PRODUCTOS ---")
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
    salida()

def actualizar_cantidad():
    productos = leer_archivo(ruta_inventario)
    mostrar_separadores()
    print("--- ACTULIZACION DE CANTIDAD DE PRODUCTOS ---")
    producto = producto_existe()
    cantidad = pedir_cantidad()

    if producto in productos:
        productos[producto]["cantidad"] = cantidad

    guardar_datos(ruta_inventario, productos)
    print(f"\033[033mCambio de cantidad de productos actualizado correctamente\033[0m")
    salida()

def eliminar_producto():
    productos = leer_archivo(ruta_inventario)
    mostrar_separadores()
    print("--- ELIMINAR UN PRODUCTO ---")
    
    producto = producto_existe()

    if producto in productos:
        productos.pop(producto)

    guardar_datos(ruta_inventario, productos)
    print(f"\033[033mProducto eliminado correctamente\033[0m")
    salida()

def calcular_valor_total():
    productos = leer_archivo(ruta_inventario)

    mostrar_separadores()
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
    salida()   

menu()