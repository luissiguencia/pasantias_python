"""
1) Localiza el error en el siguiente bloque de código. Crea una excepción para 
evitar que el programa se bloquee y además explica en un mensaje al usuario
 la causa y/o solución:
"""
print("\n----->>> 1 ")

try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: No es posible dividir por cero, debes introducir un número distinto.")

"""
2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar 
que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
"""

print("\n----->>> 2 ")

lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice al que intentas acceder se encuentra fuera del rango, debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")


"""
3) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se
 bloquee y además explica en un mensaje al usuario la causa y/o solución"""

print("\n----->>> 3 ")

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']
except KeyError:
    print("Error: La clave del diccionario no se encuentra, debes probar con otra que sí exista.")


"""
4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa
 se bloquee y además explica en un mensaje al usuario la causa y/o solución:"""

print("\n----->>> 4 ")

try:
    resultado = "20" + 15
except TypeError:
    print("Error: Sólo es posible sumar datos del mismo tipo, debes transformar el número a cadena o la cadena a número.")

"""
5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe añadir
 el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya 
 se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este 
 mensaje en su lugar:"""

print("\n----->>> 5 ")

elementos = [1, 5, -2]

def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)
        

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)

