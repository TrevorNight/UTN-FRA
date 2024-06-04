'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

4- Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

'''
def solicitar_numero_entero(mensaje, mensaje_error):
    while True:
        numero = input (mensaje)

        try:
            numero = int (numero)
            return numero
                        
        except ValueError:
            print(mensaje_error)

def solicitar_numero_flotante(mensaje, mensaje_error):
    while True:
        numero = input (mensaje)

        if "." in numero:
            try:
                numero = float (numero)
                return numero
            
            except ValueError:
                print(mensaje_error)
        else:
            print(mensaje_error)

def solicitar_cadena(mensaje, mensaje_error):
    while True:
        cadena = input (mensaje)

        if not cadena:
            print (mensaje_error)
        else:
            return cadena
