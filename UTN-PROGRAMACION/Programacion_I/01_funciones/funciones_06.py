'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

6- Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

'''
def verificar_numero_par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

#probando funcion
numero = 2
verificar = verificar_numero_par_impar(numero)
