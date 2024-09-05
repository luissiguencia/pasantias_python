# no modifiques el nombre de ninguna variable, puedes crear nuevas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234) #Se agrega al final de la lista 1
lista1.append("Hola") #Se agrega al final de la lista 1
print(lista1)
lista2.append("Adiós") 
lista2.append(1234)
print(lista2)

lista3=lista1 [:4] #Guardo en una nueva variable la lista 1 menos el último elemento
print(lista3)
lista4=lista2[1:5]
lista5=lista4+lista3 #Sumo ambas listas para guardarla en una sola variable
print(lista5)