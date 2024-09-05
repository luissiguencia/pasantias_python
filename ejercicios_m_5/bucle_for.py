sumatorio = 0
numero=8
for n in range(numero+1): #Usamos la funcion range con el numero+1 para no excluirlo de la suma total
    if(n%5 !=0 and n%7 !=0): #n será la variable para identificar el número dentro del rango de 8
        print(n)             #para así comparar que no sea múltiplo de 5 y 7
        sumatorio +=n      #Se sumarán todos los números recorridos excepto los múltiplos de 5 y 7

print(sumatorio)
