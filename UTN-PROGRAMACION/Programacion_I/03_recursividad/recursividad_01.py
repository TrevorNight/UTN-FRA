'''
nombre: Julian
apellido: Castro
---
Realizar una función recursiva que calcule la suma de los primeros números naturales:

'''
def sumar_naturales(numero: int)->int:
    if numero == 1:
        resultado = 1
    else:
        resultado = numero + sumar_naturales(numero - 1)

    return resultado