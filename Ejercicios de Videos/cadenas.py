#!/urs/bin/python3

# Texts

"""
Dadas cuatro variables con diferentes textos (cadena1, cadena2, cadena3 y cadena4) utiliza 
lo que has aprendido para generar una cadena5 con el siguiente contenido:
--> Python es un lenguaje de programación moderno
Debes generar el contenido de cadena5 utilizando como origen el texto de las 4 primeras y el 
único carácter literal que puedes escribir son espacios " "
"""

cadena1 = "moderno"
cadena2 = "Python"
cadena4 = "de programación"
cadena3 = "es un lenguaje"

cadena5 = cadena2 + " " + cadena3 + " " + cadena4 + " " + cadena1

print("[1] Textos")
print(cadena5)

# Slicing

"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto al revés. 
Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia. Realiza lo siguiente:

--> Voltea la cadena y guárdala en una variable llamada cadena_volteada. Puedes devolver una cadena volteada 
    usando un tercer índice negativo con slicing tal que así: cadena[::-1]
--> Extrae el nombre y apellido del alumno y almacénalos en una variable llamada nombre.
--> Extrae la nota y almacénala en una variable llamada nota.
--> Extrae la materia y almacénala en una variable llamada materia.
--> Genera exactamente la siguiente estructura formateando las anteriores variables en una cadena 
    llamada cadena_formateada donde nombre, nota y materia hacen referencia a las variables extraídas:
        {nombre} ha sacado un {nota} en {materia}
        Ejemplo:
        Ramón García ha sacado un 8.1 en Matemáticas

Notas y consejos:
* Todas las variables del enunciado deben existir y contener el valor correcto para pasar las pruebas.
* Utiliza slicing para extraer las porciones de la cadena que te interesan.
+ Crea tantas variables como necesites para hacerlo más sencillo.
"""

cadena_corrupta = "airotsiH,6.7,aícraG nómaR"
cadena_volteada = cadena_corrupta[::-1] # Ramón García,7.6,Historia
nombre = cadena_volteada[:12]
nota = cadena_volteada[13:16]
materia = cadena_volteada[-8:]

cadena_formateada = f"{nombre} a sacado un {nota} en {materia}" 

print("\n[2] Slicing")
print(cadena_formateada)