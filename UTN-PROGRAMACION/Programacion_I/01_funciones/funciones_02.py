'''
nombre: Julian
apellido: Castro
---
Funciones Parte I

2- Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

'''
def solicitar_numero_flotante():
    numero = input("Ingrese un numero flotante: ")
    numero = float (numero)
    return numero

#probando funcion
#numero_flotante = solicitar_numero_flotante()
#print(f"Su numero flotante es: {numero_flotante}")