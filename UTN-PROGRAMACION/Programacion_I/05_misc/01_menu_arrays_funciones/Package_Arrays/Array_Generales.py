from Especificas import *
from os import system

def mostrar_menu():
    mensaje = "Ingrese un numero entero:"
    mensaje_error = "Error, el numero debe estar entre -1000 y 1000"
    minimo = -1000
    maximo = 1000
    cantidad_numeros = 10

    lista_numeros = pedir_numeros_enteros(mensaje, mensaje_error, minimo, maximo, cantidad_numeros)

    while True:
        
        menu =  ("1_Mostrar la cantidad de números positivos y negativos.\
                \n2_Mostrar la sumatoria de los números pares.\
                \n3_Informar el mayor de los números impares.\
                \n4_Listar todos los números ingresados.\
                \n5_Listar todos los números pares.\
                \n6_Listar los números de las posiciones impares.\
                \n7_Salir.\
                \nElija una opcion:")

        opcion = input(menu)

        match opcion:
            case "1":
                numeros_positivos = 0
                numeros_negativos = 0
                    
                for posicion in range(cantidad_numeros):
                    numero = determinar_positivo_negativo(lista_numeros[posicion])

                    if numero:
                        numeros_positivos = numeros_positivos + 1
                    else:
                        numeros_negativos = numeros_negativos + 1
                
                print (f"Numeros positivos: {numeros_positivos} \
                    \nNumeros negativos: {numeros_negativos}")
                
            case "2":
                suma_pares = sumar_numeros_pares(lista_numeros, cantidad_numeros)
                print(suma_pares)

            case "3":
                numero_impar_mayor = mostrar_numero_impar_mayor(lista_numeros, cantidad_numeros)
                print(numero_impar_mayor)

            case "4":
                mostrar_lista(lista_numeros)
            case "5":
                cantidad_pares = contar_pares(lista_numeros, cantidad_numeros)
                lista_pares = [0] * cantidad_pares
                posicion2 = -1
                for posicion in range(cantidad_numeros):
                    if lista_numeros[posicion] % 2 == 0:
                        posicion2 = posicion2 + 1
                        lista_pares[posicion2] = lista_numeros[posicion]
                mostrar_lista(lista_pares)
            
            case "6":
                lista_posicion_impares = listar_posicion_numeros_impares(lista_numeros, cantidad_numeros)
                mostrar_lista(lista_posicion_impares)

            case "7":
                break

        system("pause")    
        system("cls")

mostrar_menu()