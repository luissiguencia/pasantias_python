"""
1) Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a partir 
de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura.

Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura."""

print("----->>> 1 ")

def area_rectangulo(base, altura):
    return base*altura

print(area_rectangulo(base=25, altura=10))

"""
*2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
 Calcula el área de un círculo de 5 de radio: *

Nota: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el 
número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:"""

print("\n----->>> 2 ")

import math

def area_circulo(radio):
    return (radio**2) * math.pi

print( area_circulo(5))

"""
3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
** Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'**"""

print("\n----->>> 3 ")

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
print( relacion(5, 10) )
print( relacion(10, 5) )
print( relacion(5, 5) )

"""
4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

** Comprueba el punto intermedio entre -12 y 24**"""

print("\n----->>> 4 ")

def intermedio(num_1, num_2):
    return (num_1 + num_2) / 2

print(intermedio(-12, 24))

"""
5) Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número 
a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá q
ue cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
** Comprueba el resultado de recortar 15 entre los límites 0 y 10**"""

print("\n----->>> 5 ")

def recortar(n, i, s):
    if n < i:
        return i
    elif n > s:
        return s
    return n

print(recortar(15, 0, 10))

"""
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:"""

print("\n----->>> 6 ")

numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(enteros):
    enteros.sort()
    pares = []
    impares = []
    for numero in enteros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)


