def recortar(numero,minimo,maximo): #La función recibirá 3 parámetros
    if numero<minimo:               #Se retornará cada uno en caso que cumplan las condiciones
        return minimo
    elif numero>maximo:
        return maximo
    else:
        return numero