'''
nombre: Julian
apellido: Castro
---
Escribir una función que reciba como parámetros una
lista de enteros y retorne la posición del valor máximo encontrado.
'''
def encontrar_posicion_maximo(lista_enteros:list) -> int|None:
    primer_numero = True
    posicion_maximo = None
    
    if type(lista_enteros) == list:
        len_lista = len(lista_enteros)

        for posicion in range(len_lista):
            if type(lista_enteros[posicion]) == int:
                if primer_numero or numero_maximo < lista_enteros[posicion]:
                    numero_maximo = lista_enteros[posicion]
                    posicion_maximo = posicion
                    primer_numero = False
    
    return posicion_maximo