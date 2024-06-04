'''
nombre: Julian
apellido: Castro
---
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    pass
    
En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

Repetir el mismo procedimiento para un dato de tipo float.

'''
def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    while True:
        numero = input (mensaje)

        try:
            numero = int (numero)

            if numero <= maximo and numero >= minimo:
                return numero
            else:
                print(mensaje_error)
                reintentos = reintentos - 1
                        
        except ValueError:
            print(mensaje_error)
            reintentos = reintentos - 1

        if reintentos < 0:
            return None

def get_float(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:
    while True:
        numero = input (mensaje)

        if "." in numero:
                try:
                    numero = float (numero)

                    if numero <= maximo and numero >= minimo:
                        return numero
                    else:
                        print(mensaje_error)
                        reintentos = reintentos - 1
                        
                except ValueError:
                    print(mensaje_error)
                    reintentos = reintentos - 1
        else:
            print(mensaje_error)
            reintentos = reintentos - 1
        
        if reintentos < 0:
            return None
        
#probar funcion
#mensaje = "Ingrese un numero: "
#mensaje_error = "¡Error! Dato invalido"
#minimo = 5
#maximo = 10
#reintentos = 1

#numero = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)

#print(f"Este es su numero: {numero}")
