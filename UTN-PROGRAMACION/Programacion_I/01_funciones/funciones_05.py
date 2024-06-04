'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

5- Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

'''
import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

#probando funcion
radio = 5
area = calcular_area_circulo(radio)
print (area)
