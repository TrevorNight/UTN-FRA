'''
nombre: Julian
apellido: Castro
---
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

'''
def calcular_fibonacci(numero:int)->int:
    if numero < 1:
        return numero
    elif numero < 2:
        return numero
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

    return resultado