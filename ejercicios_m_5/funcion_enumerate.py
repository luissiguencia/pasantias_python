iniciales= ["Hola","Mundo"]

#i es el índice, y cadena hace referencia al elemento o cada palabra en la lista
for i,cadena in enumerate(iniciales): #Usamos la función enumerate para recorrer cada cadena dentro de la lista iniciales
    # Modificamos cada cadena por su letra inicial
    iniciales[i] = iniciales[i][0]    

print(iniciales)