from Package_Input.Input import *
    
def pedir_numeros_enteros(mensaje:str, mensaje_error:str, minimo:int, maximo:int, cantidad_numeros:int) -> list:
    lista_numeros = [0] * cantidad_numeros
    for posicion in range(cantidad_numeros):
        print(posicion + 1, "° numero ")
        numero = None
        while numero == None:
            numero = get_int(mensaje, mensaje_error, minimo, maximo, 0)                      
        lista_numeros[posicion] = numero

    return lista_numeros

def determinar_positivo_negativo(numero) -> True|False :
    if numero < 0:
        return False
    else:
        return True

def sumar_numeros_pares(lista_numeros:list, cantidad_numeros:int) -> int:
    suma_pares = 0
    for posicion in range(cantidad_numeros):
        if lista_numeros[posicion] % 2 == 0:
            suma_pares = suma_pares + lista_numeros[posicion]
    
    return suma_pares

def mostrar_numero_impar_mayor(lista_numeros:list, cantidad_numeros:int) -> int:
    primer_numero = True
    for posicion in range(cantidad_numeros):
        if lista_numeros[posicion] % 2 != 0:
            if primer_numero or numero_impar_mayor < lista_numeros[posicion]:
                numero_impar_mayor = lista_numeros[posicion]
                primer_numero = False
    
    return numero_impar_mayor

def contar_pares(lista_numeros:list, cantidad_numeros:int) -> int:
    cantidad_pares = 0
    for posicion in range(cantidad_numeros):
        if lista_numeros[posicion] % 2 == 0:
            cantidad_pares = cantidad_pares + 1
    
    return cantidad_pares

def mostrar_lista (lista:list):
    len_lista = len(lista)
    for posicion in range(len_lista):
        print(lista[posicion])

def listar_posicion_numeros_impares(lista_numeros:list , cantidad_numeros:int) ->list:
    cantidad_impares = 0
    for posicion in range(cantidad_numeros):
        if lista_numeros[posicion] % 2 != 0:
            cantidad_impares = cantidad_impares + 1
    
    lista_posicion_impares = [0] * cantidad_impares
    posicion2 = -1
    for posicion in range(cantidad_numeros):
        if lista_numeros[posicion] % 2 != 0:
            posicion2 = posicion2 + 1
            lista_posicion_impares[posicion2] = posicion

    return lista_posicion_impares
    

