#!/usr/bin/pythob3

### !------>> TUPLAS

"""
A partir de una variable llamada tupla (la cuál no sabes qué contiene) debes imprimir por 
pantalla los siguientes apartados (usando un print() para cada apartado), de forma ordenada:

--> El último elemento de la tupla.
--> El número de elementos que tiene la tupla.
--> La posición donde se encuentra el número 123 de la tupla.
--> Una lista con los primeros tres elementos de la tupla.
--> El elemento que hay en la posición con índice 4 de la tupla.
--> El número de veces que aparece el número 4 en la tupla.

Nota: En total son 6 prints uno debajo de otro, no puedes redefinir ni modificar la tupla o el test fallará,
simplemente muestra lo que se pide por pantalla.
"""
tupla = (123, "hola", [1, 2, 3], 3, "mundo", (7, 8), True, None, {"clave": "valor"}, 9)

print(tupla[-1])
print(len(tupla))
print(tupla.index(123))
print(list(tupla[:3]))
print(tupla[4])
print(tupla.count(4))

### !------>> SETS

"""
El siguiente ejercicio te servirá para practicar la manipulación de conjuntos.
Debes realizar las siguientes instrucciones de forma ordenada sobre la variable grupo para que el ejercicio valide correctamente:
--> Añade los siguientes usuarios: Ana, Ramón, Marta, Eric y David (respeta las tildes)
--> Elimina (*) los usuarios Mario, Miguel y Ramón.
--> Optativo: Cuando tu solución valide, dale una vuelta de tuerca. A ver si se te ocurre alguna forma de optimizarlo utilizando listas y bucles.

(*) Para eliminar un registro de un conjunto puedes utilizar su método interno conjunto.remove("registro").
"""

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# grupo.add('Ana')
# grupo.add('Ramón')
# grupo.add('Marta')
# grupo.add('Eric')
# grupo.add('David')

others = ["Ana", "Ramón", "Marta", "Eric", "David"]
grupo.update(others)

# grupo.remove("Mario")
# grupo.remove("Miguel")
# grupo.remove("Ramón")

rid = ["Mario", "Miguel", "Ramón"]
for usuario in rid:
    grupo.discard(usuario)

print(grupo)

### !------>> DICTIONaries

"""
El siguiente ejercicio te servirá para practicar la manipulación de diccionarios.
Debes realizar las siguientes instrucciones de forma ordenada sobre la variable animales para que el ejercicio valide correctamente:
--> Añade al diccionario las claves perro, gato y rana con sus respectivos valores dog, cat y frog.
--> Modifica las claves caballo y vaca con los valores horse y cow respectivamente.
--> Por último elimina del diccionario las claves rana y vaca.
"""

animales = {"caballo":"", "vaca":""}

animales.update({"perro": "dog", "gato" : "cat", "rana" : "frog"})

animales["caballo"] = "hourse"
animales["vaca"] = "cow"

del(animales["rana"])
del(animales["vaca"])

print(animales)
