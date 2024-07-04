from .Validate import *

def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    while True:
        cadena = input (mensaje)
        numero_validado = validate_number (cadena, minimo, maximo)

        if numero_validado and not cadena in ".":
            numero_entero = int(cadena)
            return numero_entero

        else:
            print (mensaje_error)
            reintentos = reintentos - 1
        
        if reintentos < 0:
            return None

def get_float(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:
    while True:
        cadena = input (mensaje)
        numero_validado = validate_number (cadena, minimo, maximo)

        if numero_validado:
            numero_flotante = float(cadena)
            return numero_flotante

        else:
            print (mensaje_error)
            reintentos = reintentos - 1
        
        if reintentos < 0:
            return None

def get_string(mensaje:str, mensaje_error:str, longitud: int, reintentos:int) -> str|None:
    while True:
        cadena = input (mensaje)
        cadena_validado = validate_length (cadena, longitud)

        if cadena_validado:
            return cadena
        else:
            print (mensaje_error)
            reintentos = reintentos - 1
            if reintentos < 0:
                return None