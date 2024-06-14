'''
nombre: Julian
apellido: Castro
---
Realizar una función recursiva que la suma de los dígitos de un número:

'''
def sumar_digitos(numero:int)->int:
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        resultado = ultimo_digito + sumar_digitos(numero // 10)

    return resultado