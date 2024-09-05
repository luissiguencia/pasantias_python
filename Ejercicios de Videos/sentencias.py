#!/usr/bin/python3

"""
Condiciones
Utilizando una condición if-elif-else debes realizar un programa que compare la longitud de dos 
variables (cadena_1 y cadena_2) y en función del resultado almacene un valor en otra variable llamada resultado:

Si cadena_1 es más larga que cadena_2 la variable resultado deberá tener el valor entero 1.
Si cadena_1 es más corta que cadena_2 la variable resultado deberá tener el valor entero 2.
Si cadena_1 tiene la misma longitud que cadena_2 la variable resultado deberá tener el valor entero 0.

Notas:
Las variables cadena_1 y cadena_2 se importan de otro fichero y no puedes editarlas.
Recuerda que puedes conseguir la longitud de una cadena usando len(cadena)
"""
cadena_1 = "Oasis"
cadena_2 = "Desierto"

resultado = 0

if len(cadena_1) > len(cadena_2):
    resultado = 1
elif len(cadena_1) < len(cadena_2):
    resultado = 2
elif len(cadena_1) == len(cadena_2):
    resultado = 0

print(resultado)