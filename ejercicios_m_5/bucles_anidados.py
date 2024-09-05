matriz=[
    [8,7,0],
    [24,2,-1],
    [9,-5,12]
]

# Completa el ejercicio aquí
for i,fila in enumerate(matriz): #Se usa enumerate para poder recorrer el índice de cada elemento, en este caso de las filas
    for j,columna in enumerate(fila): #Aquí recorre las columnas de la tabla o sublistas
        if(matriz[i][j] % 2 == 0): #Aquí comprobamos si en las filas y columnas hay números pares
            matriz[i][j]=0         #Si hay, pasará a reemplazarlos por 0
        else:
            matriz[i][j]=1         #Sino, los reemplazará por 1
        
        print("[",matriz[i][j],"]", end="")
    print()

