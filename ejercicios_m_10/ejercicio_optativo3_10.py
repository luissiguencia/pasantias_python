colores = {'rojo':'red', 'verde':'green', 'negro':'black'}

try:
    colores['blanco']
except KeyError:
    print("Error: La palabra clave que ingresó no existe dentro del diccionario")