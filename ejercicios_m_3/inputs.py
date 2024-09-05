# Completa el ejercicio
#Nombre 
nombre= input("Escribe tu nombre: ")
apellido= input("Escribe tu apellido: ")
edad= int(input("Introduce tu edad: "))
numero_magico=float(input("Introduce un número cualquiera: "))

cadena_final=nombre+" "+apellido+": Tu número de la suerte es el "+str(edad*numero_magico)
print(cadena_final)