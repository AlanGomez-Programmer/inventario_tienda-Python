import os
from json import load, dumps, dump

def mostar_separadores():
    os.system("clear")
    print("="*40)

# FUNCIONES PARA LA PERSISTENCIA DE DATOS

ruta_inventario = "inventario.json"

def leer_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            datos = load(archivo)
            return datos
    except FileNotFoundError:
        print("\033[31mERROR: No existe el archivo \033[0m")
        
        with open(ruta, "w") as archivo:
            dump({}, archivo)
            print("\033[34mSe ha creado un archivo llamado inventario.json\033[0m")
            return {}
    
def guardar_datos(ruta, datos):
    try:
        with open(ruta, "w") as archivo:
            archivo.write(dumps(datos, indent= 4))
    except Exception:
        print("\033[31mError inesperado al guardar \033[0m")

# VALIDACIONES

def pedir_num_enteros(mensaje):
    while True:
        try:
            numero = int(input(mensaje).strip())
            
            if numero <= 0:
                print("\033[31mERROR: El número debe ser mayor a 0\033[0m")
                continue
            else:
                return numero
        except ValueError:
            print("\033[31mERROR: Solo se aceptan numeros enteros \033[0m")

def pedir_letras(mensaje):
    while True:
        texto = input(mensaje).strip()
        
        solo_letras = all(c.isalpha() or c.isspace() for c in texto)

        if not solo_letras:
            print(f"\033[031mERROR: Solo se permiten letras \033[0m")
            continue

        if texto == "":
            print(f"\033[031mERROR: No se permite dejar en blanco este apartado \033[0m")
            continue

        if texto:
            return texto.title()

def validar_producto():
    productos = leer_archivo(ruta_inventario)
    while True:
        producto = pedir_letras("PRODUCTO: ").strip().capitalize()
        
        if producto in productos:
            print(f"\033[031mERROR: Ese producto ya existe \033[0m")
        else:
            return producto

def pedir_precio():
    while True:
        try:
            precio = float(input("PRECIO: "))
            
            if precio <= 0:
                print(f"\033[031mERROR: El precio degbe ser mayor a 0 \033[0m")
                continue
            else:
                return precio
        except ValueError:
            print(f"\033[031mERROR: Solo se permiten numeros decimales \033[0m")

def pedir_cantidad():
  while True:
        try:
            cantidad = int(input("CANTIDAD: "))
            
            if cantidad <= 0:
                print(f"\033[031mERROR: La cantidad de productos debe se mayor a 0 \033[0m")
                continue
            else:
                return cantidad
        except ValueError:
            print(f"\033[031mERROR: Solo se permiten numeros enteros \033[0m")
