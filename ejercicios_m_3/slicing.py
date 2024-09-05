# Variables del ejercicio
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Completa el ejercicio
cadena_volteada = cadena_corrupta[::-1]
print(cadena_volteada) #Confirmo que se ha volteado la cadena
print(len(cadena_volteada))  #Imprimo la longitud de la cadena para saber cuantas posiciones hay

#Se extrae de cada rango la palabra para guardarla en una nueva variable
nombre=cadena_volteada[0:12]
nota=cadena_volteada[13:16]
materia=cadena_volteada[17:25]
cadena_formateada =nombre+" ha sacado un " +nota+" en " +materia
print(cadena_formateada)