def validate_number(cadena, minimo, maximo):
    if cadena.isdigit():
        numero_validado = True
    
    elif cadena[0] in ("-", "+"):
        numero_validado = cadena[1:].isdigit()
    
    elif cadena in ".":
        cadena_modificada = cadena.replace(".", "", 1)
        numero_validado = cadena_modificada.isdigit()

    else:
        return False
    
    if not numero_validado:
        return False
    
    numero = float (cadena)
    if numero < minimo or numero > maximo:
        return False
    else:
        return True

def validate_length(cadena, longitud):
    cadena_len = len(cadena)
    if cadena_len > longitud:
        return False
    else:
        return True