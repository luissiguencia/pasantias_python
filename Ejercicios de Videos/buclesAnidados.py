#!/usr/bin/python3

"""
Bucles anidados
En este ejercicio se te va a facilitar una variable matriz repleta de números
 enteros y de la cuál lo único que sabes es que contiene dos dimensiones.
 Aquí tienes una estructura de ejemplo ilustrando como se forma (lista con 
 sublistas), muy parecida a una tabla:
        matriz = [
                    [8,  7,  0],
                    [34, 2, -1],
                    [5, -5, 12]
                ]
El objetivo del ejercicio es modificar su contenido dinámicamente, sustituyendo 
todos sus números pares por 0 y los impares por 1.

Notas:
--> Una forma de entender una matriz bidimensional es como una tabla compuesta de filas y columnas.
--> Las filas y columnas se representan como listas anidadas y eso significa que se pueden recorrer mediante bucles for anidados.
--> Comúnmente al índice que recorre las filas se le denomina i y al de las columnas j, tal como muestra la imagen inferior.
--> Para acceder a una posición dinámicamente será necesario entonces utilizar ambos índices, tal que así: matriz[i][j]
--> Recuerda utilizar la función enumerate para conseguir los índices, teniendo en cuenta que primero se recorren las 
    filas y de ellas las columnas, siendo cada columna el propio valor a tratar.
"""

matriz = [
            [8,  7,  0],
            [34, 2, -1],
            [5, -5, 12]
        ]

for i, row in enumerate(matriz):
    for j, element in enumerate(row):
        if element % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1

print(matriz) # [[0, 1, 0], [0, 0, 1], [1, 1, 0]]