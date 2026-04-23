import os

def mostar_separadores():
    os.system("clear")
    print("="*40)


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
