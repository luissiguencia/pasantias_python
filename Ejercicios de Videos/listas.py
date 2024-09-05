#!/urs/bin/python3

"""
Dadas dos listas lista1 y lista2 debes realizar diferentes tareas por el orden indicado:
--> Añade a la lista1 el número 1234 y luego el texto Hola.
--> Añade a la lista2 el texto Adiós y luego el número 1234.
--> Genera una lista3 con todos los elementos de la lista1 excepto el último.
--> Genera una lista4 con todos los elementos de la lista2 excepto el primero y el último.
--> Genera una lista5 con los elementos de la lista4 más la lista3
"""

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append(1234)
lista1.append("Hola") # [1, 12, 123, 1234, 'Hola']

lista2.append("Adios")
lista2.append(1234) # ['Bye', 'Ciao', 'Agur', 'Adieu', 'Adios', 1234]

lista3 = lista1[:4] # [1, 12, 123, 1234]
lista4 = lista2[1:5] # 'Ciao', 'Agur', 'Adieu', 'Adios']

lista5 = lista4 + lista3 # ['Ciao', 'Agur', 'Adieu', 'Adios', 1, 12, 123, 1234]

print(lista5)



