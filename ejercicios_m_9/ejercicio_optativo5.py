def recortar(numero,inferior,superior): #La función recibirá 3 parámetros para cumplir cada condición
    if numero<inferior:
        return inferior
    if numero>superior:
        return superior
    else:
        return numero

print(recortar(15,0,10))