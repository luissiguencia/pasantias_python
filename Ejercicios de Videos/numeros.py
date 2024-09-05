#!/urs/bin/python3

# print() function
"""
Una funcionalidad que encontramos en todos los lenguajes es la de imprimir un valor por pantalla. 
En Python esa función se llama print() y debemos pasar el valor o literal entre los paréntesis. 
Modifica el código del ejercicio para que el resultado mostrado sea el siguiente:
123
-21
3.14
999.999
100
777
"""
print("\n[1] print() Function" )

print(123)
print(-21)
print(3.14)
print(999.999)
print(100)
print(777)

# Variables

"""
Un profesor quiere calcular la nota final de sus alumnos en base a dos exámenes y está 
desarrollando un algoritmo, el problema es que los exámenes cuentan diferente y no sabe 
cómo acabar el programa:

El primer examen nota_1 cuenta un 40% de la nota final.

El segundo examen nota_2 cuenta un 60% de la nota final.

Modifica las instrucciones donde creas oportuno para ayudar al profesor a conseguir 
correctamente la nota_final (no cambies el nombre de esta variable).
"""

nota_1 = 10
nota_2 = 6

final_grade = (nota_1 * 0.4) + (nota_2 * 0.6)

print("\n[2] Variable")
print(final_grade)