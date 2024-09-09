#Transformar  el texto con el uso de cademas,listas y métodos internos
texto= "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
lineas = texto.split("#") #Primero separamos las cadenas donde se encuentre el #

for i, linea in enumerate(lineas): #Recorremos con un enumerate ya que ahora se ha creado una lista con cada cadena
    lineas[i] = linea.capitalize() #Cada elemento o línea empezará con una mayúscula haciendo uso de capitalize()
   
    if i == 0: #Ya que la primera línea es diferente a las demás, hacemos la condición con su índice igual 0 para que modifique únicamente la primera línea
        lineas[i] = lineas[i] + "..." 
    else:
        lineas[i] = "- " + lineas[i] + "." #En el caso de las demás líneas, empezarán con un guión(-) y terminarán con un punto

for linea in lineas: #Finalmente recorremos las líneas para mostrarlas una por una y ver el resultado final
    print(linea)