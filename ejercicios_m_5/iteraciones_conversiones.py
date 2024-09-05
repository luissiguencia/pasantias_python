multiplos = [] #Creamos una variable con una lista vacía

# Completa el ejercicio 
numero = int(input()) 
while numero<1 or numero>9: #Se compara que el número ingresado esté entre 1 y 9 sino se deberá ingresar de nuevo
    numero=int(input())
    
multiplos=list(range(numero,101,numero)) #Sintaxis de la función range (min,max,salto)
#Min: en este caso será el número más pequeño, será el número ingresado
#Max: range recorre todos los números pero excluye el mayor, por eso se agrega uno más para que incluya el 100
#Salto: Cada que rango se mostrarán los números, que vendría a ser el mismo número ingresado

print(multiplos)