'''
nombre: Julian
apellido: Castro
---
Teniendo en cuenta la función del punto 1, crear la función get_string. 
La misma validará la longitud de la cadena ingresada dado 
el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
def get_string(longitud: int) -> str|None:
    pass
Nota: utilizar la función len.
'''
def get_string(mensaje:str, mensaje_error:str, longitud: int, reintentos:int) -> str|None:
    while True:
        cadena = input (mensaje)
        cadena_len = len(cadena)

        if not cadena or cadena_len > longitud:
            print (mensaje_error)
            reintentos = reintentos - 1
        else:
            return cadena
        
        if reintentos < 0:
            return None
