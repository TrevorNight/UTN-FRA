'''
nombre: Julian
apellido: Castro
---
Escribir una función que calcule y 
retorne el producto de todos los elementos de la lista que recibe como parámetro.
'''
def calcular_producto(lista):
    resultado = 1
    len_lista = len(lista)

    for i in range(len_lista):
        resultado = resultado * lista[i]
    
    return resultado