#!/usr/bin/python3

"""
Bucle while
Realiza un programa que lea un número por teclado y lo almacene en una variable llamada numero.
Si ese número introducido por teclado no es múltiple de 5 debe repetirse de nuevo la lectura hasta que lo sea.
Notas:
Debes asegurarte de que la variable numero es un número entero introducido con la instrucción input.
Si intentas asignar un múltiple de 5 manualmente a la variable numero la solución fallará.
"""

import random


numero = -2

while numero % 5 != 0:
    numero = int(input())

"""
Bucle for
En este ejercicio se te facilitará un numero aleatorio que no conoces en la variable numero.
Utilizando lo que conoces sobre los bucles for y la función range() , debes realizar un sumatorio
de todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples 
de 5 y 7, y almacenarlo en la variable sumatorio.
Ejemplo, si numero fuera 7, el sumatorio sería igual a 1+2+3+4+6 = 16.

Recuerda, únicamente debes sumar los números NO múltiples de 5 y 7 al sumatorio.
"""

sumatorio = 0

for n in range(random.randint(1, 15) + 1):
    if(n % 5 != 0 and n % 7 != 0):
        print(n)
        sumatorio +=n

print(f"Sumatoria es {sumatorio}")





