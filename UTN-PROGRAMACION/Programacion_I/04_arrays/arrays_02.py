'''
nombre: Julian
apellido: Castro
---
Escribir una función parecida a la anterior, 
pero la misma deberá calcular y devolver el promedio de los números positivos.
'''
def calcular_promedio_positivos(lista_enteros:int):
    resultado = 0
    numeros_positivos = 0
    len_lista = len(lista_enteros)

    for i in range(len_lista):
        if lista_enteros[i] > 0:
            resultado = resultado + lista_enteros[i]
            numeros_positivos = numeros_positivos + 1

    if resultado == 0:
        return resultado

    promedio_positivos = resultado / numeros_positivos
    return promedio_positivos