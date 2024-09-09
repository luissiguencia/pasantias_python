numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista_numeros):
    lista_numeros.sort() #Aquí ordenamos los elementos dentro de la lista que recibe la función
    pares= []            #Creamos dos listas vacías donde se añadirán los elementos por separado
    impares = []

    for i in lista_numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares #El tipo de dato que se devuelva debe ser el mismo que el del parámetro que se envía en la función
                         #En este caso devolverá una lista con los números pares, y otra con los impares
print(separar(numeros))