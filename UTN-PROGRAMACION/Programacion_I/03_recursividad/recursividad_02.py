'''
nombre: Julian
apellido: Castro
---
Realizar una función recursiva que calcule la potencia de un número:

'''
def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 0:
        resultado = 1
    elif exponente == 1:
        resultado = base
    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado