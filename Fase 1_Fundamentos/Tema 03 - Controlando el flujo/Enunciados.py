"""
1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""

n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Digita tu opcion: ") )     

if opcion == 1:
    print(f"La suma de {n1} + {n2} es {n1+n2}")
elif opcion == 2:
    print(f"La resta de {n1} + {n2} es {n1+n2}")
elif opcion == 3:
    print(f"El producto de {n1} * {n2} es {n1*n2}")
else:
    print("Opción incorrecta")

"""
2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
"""

numero = 0
while numero % 2 == 0:
    numero = int(input("Introduce un número impar: ") )


"""
3) Realiza un programa que sume todos los números pares desde el 0 hasta el 100:

Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
"""

suma = sum( range(0, 101, 2) )
print(suma)


"""
Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
"""

suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)

"""
5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
"""

numeros = [1, 3, 6, 9]

while True:
    numero = int(input("Escribe un número del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break

if numero in numeros:
    print("El número",numero,"se encuentra en la lista",numeros)
else:
    print("El número",numero,"no se encuentra en la lista",numeros)

"""
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).
"""

print( list( range( 0, 11 ) ) )
print( list( range( -10, 1 ) ) )
print( list( range( 0, 21, 2 ) ) )
print( list( range( -19, 0, 2 ) ) )
print( list( range( 0, 51, 5 ) ) )

"""
7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:
"""

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)

# lista_3 = lista_1 = lista_2
# list_5 = list(set(lista_3))
# print(list_5)