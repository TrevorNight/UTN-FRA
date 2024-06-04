'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

7- Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

'''
def encontrar_numero_maximo(numero_a, numero_b, numero_c):
    if numero_a > numero_b and numero_a > numero_c:
        numero_maximo = numero_a
    elif numero_b > numero_c:
        numero_maximo = numero_b
    else:
        numero_maximo = numero_c
    return numero_maximo

#probando funcion
numero_a = 1
numero_b = 2
numero_c = 3
numero_maximo = encontrar_numero_maximo(numero_a, numero_b, numero_c)
print(numero_maximo)