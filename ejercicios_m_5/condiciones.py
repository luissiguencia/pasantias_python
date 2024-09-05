# Variables del ejercicio (no las edites)
cadena_1="Hola mundo"
cadena_2="Python"

# Completa el ejercicio a partir de aquí

if len(cadena_1)> len(cadena_2): #Comparo si la longitud de cadena1 es mayor a cadena2
    resultado=1
if len(cadena_1)< len(cadena_2): #Comparo si la longitud de cadena1 es menor a cadena2
   resultado=2
if len(cadena_1) == len(cadena_2): #Comparo si la longitud de ambas cadenas es igual
   resultado=0

print(resultado)