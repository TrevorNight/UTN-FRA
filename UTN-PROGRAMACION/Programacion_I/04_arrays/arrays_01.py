'''
nombre: Julian
apellido: Castro
---
Escribir una función que reciba una lista de enteros, 
la misma calculará y devolverá el promedio de todos los números.
'''
def calcular_promedio(lista_enteros:int):
    resultado = 0
    len_lista = len(lista_enteros)

    for i in range(len_lista):
        resultado = resultado + lista_enteros[i]
    
    promedio = resultado / len_lista
    return promedio