'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

8- Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

'''
def calcular_potencia_numero(base, exponente):
    resultado = base ** exponente
    return resultado

#probando funcion
base = 5
exponente = 2
resultado = calcular_potencia_numero(base, exponente)
print (resultado) 