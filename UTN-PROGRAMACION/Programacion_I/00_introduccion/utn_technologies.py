'''
nombre: Julian
apellido: Castro
---
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

https://onlinegdb.com/V45s68BH9

'''
empleados_iot_ia = 0
empleados_no_ia = 0
edad_empleado_mayor = 0

for contador_encuestas in range (1,11):
    print ("Encuesta:", contador_encuestas)
    nombre = input ("Ingrese su nombre: ")

    edad = input ("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input ("Reingrese su edad: ")
        edad = int(edad)

    genero = input ("Ingrese su genero: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input ("Reingrese su genero(Masculino, Femenino, Otro): ")

    tecnologia = input ("Ingrese su tecnologia: ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input ("Reingrese su tecnologia(IA, RV/RA, IOT): ")
    
    if genero == "Masculino":
        if edad > 24 and edad < 51:

            if tecnologia == "IA" or tecnologia == "IOT":     
                empleados_iot_ia = empleados_iot_ia + 1
        
            if edad > 32 and edad < 41 and tecnologia != "IA":
                empleados_no_ia = empleados_no_ia + 1

        if edad > edad_empleado_mayor:
            nombre_empleado_mayor = nombre
            edad_empleado_mayor = edad
            tecnologia_empleado_mayor = tecnologia

porcentaje_empleados_no_ia = (empleados_no_ia / contador_encuestas) * 100

mensaje = f"Empleados masculinos que votaron por IOT o IA: {empleados_iot_ia} \
    \nPorcentaje de empleados que no votaron por IA: {porcentaje_empleados_no_ia} % \
    \nNombre del empleado con mayor edad: {nombre_empleado_mayor} \
    \nTecnologia del empleado con mayor edad: {tecnologia_empleado_mayor}"

print (mensaje)