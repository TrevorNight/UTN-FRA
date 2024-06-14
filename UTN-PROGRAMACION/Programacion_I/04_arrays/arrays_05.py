'''
nombre: Julian
apellido: Castro
---
Escribir una función que reciba como parámetros una 
lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''
def encontrar_posiciones_maximos(lista_enteros:list):
    primer_numero = True
    lista_posiciones = None
    
    if type(lista_enteros) == list:
        len_lista = len(lista_enteros)
        cantidad_maximos = 1

        for i in range(len_lista):
            if type(lista_enteros[i]) == int:

                if primer_numero or numero_maximo < lista_enteros[i]:
                    numero_maximo = lista_enteros[i]
                    primer_numero = False

                elif numero_maximo == lista_enteros[i]:
                    cantidad_maximos = cantidad_maximos + 1
        
        lista_posiciones = [0] * cantidad_maximos
        posicion = -1

        for i in range(len_lista):
            if numero_maximo == lista_enteros[i]:
                posicion = posicion + 1
                lista_posiciones[posicion] = i

    print(lista_posiciones)