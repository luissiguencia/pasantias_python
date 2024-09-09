lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

def modificar(l):
    l = list(set(l))
    l.sort(reverse=True)
    
    lista_temporal =[]
    for n in l:
        if n%2==0:
           lista_temporal.append(n)
    
    suma = sum(lista_temporal)
    print("La suma de los números dentro de la lista es: ", suma)
    lista_temporal.insert(0, suma)
    return lista_temporal

nueva_lista = modificar(lista) 

print(lista)
print(nueva_lista)