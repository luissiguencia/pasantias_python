import sys

if len(sys.argv) == 2:
    numero= int(sys.argv[1]) #El numero ingresado se ubicará en el índice 1 porque el 0 es la ruta del archivo
    if numero <0 or numero > 9999: #Se compara que el número ingresado no sea menor o mayor a 0 y 9999
        print ("Error-Número incorrecto") #Imprimimos un error en caso que suceda
        print ("Ejemplo: ejercicio_optativo3.py [0-9999]")
    else:

        cadena=str(numero) #Guardamos el número ingresado en una cadena seteandolo a un string para que no de error
        longitud= len(cadena) #Sacamos la longitud de la cadena y la guardamos en la variable

        for i in range(longitud): #Recorremos la longitud de la cadena con range
            print("{:04d}".format(int(cadena[longitud-1-i])*10 ** i)) #Imprimimos el número ingresado formateado
                                                                #Estará alineado en 4 dígitos, los espacios se rellenan con 0
                                                                #Seteamos la cadena a un entero
                                                                #Se irá restando la longitud -1 y -i para voltear la cadena
                                                                #Se irá mulplicando por 10 para que cada número de la cadena aumente una unidad
                                                                #Así el número final estará alineado por unidades, decenas, centenas y milésimas 
else:
    print("Error-Argumentos erróneos")
    print("Ejemplo: ejercicio_optativo3.py [0-9999]")