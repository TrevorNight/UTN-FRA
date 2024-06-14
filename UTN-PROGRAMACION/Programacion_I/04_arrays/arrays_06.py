'''
nombre: Julian
apellido: Castro
---
Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, 
un nombre a reemplazar y su correspondiente reemplazo. 
La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con 
su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.
'''
def reemplazar_nombres(lista_nombres:list, nombre_reemplazar:str, nombre_reemplazo:str)->int|None:
    cantidad_reemplazos = None

    if type(lista_nombres) == list and type(nombre_reemplazar) == str and type(nombre_reemplazo) == str:
        cantidad_reemplazos = 0
        len_lista = len(lista_nombres)

        for posicion in range(len_lista):
            if lista_nombres[posicion] == nombre_reemplazar:
                lista_nombres[posicion] = nombre_reemplazo
                cantidad_reemplazos = cantidad_reemplazos + 1

    return cantidad_reemplazos