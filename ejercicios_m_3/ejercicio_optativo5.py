matriz= [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]
#Corrección de las sumas de cada fila del último elemento
matriz[1][-1]=sum(matriz[1][:-1])
matriz[3][-1]=sum(matriz[3][:-1])

print(matriz)

