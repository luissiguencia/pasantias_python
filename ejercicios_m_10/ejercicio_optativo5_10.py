elementos =[1,5,-2]
#Función que recibirá una lista y un elemento
def agregar_una_vez(list,element):
    try:
        if element in list: #Si el elemento que recibe está dentro de la lista nos dará un ValueError
            raise ValueError
        else:
            list.append(element) #Sino, lo agregará automáticamente dentro de la lista
    except ValueError:
        print("Error: No se pueden ingresar elementos duplicados => {}".format(element))

agregar_una_vez(elementos,10)
agregar_una_vez(elementos,-2)
agregar_una_vez(elementos,"Hola")