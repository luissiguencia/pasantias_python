"""
1) Formatea los siguientes valores para mostrar el resultado indicado:

"Hola Mundo" → Alineado a la derecha en 20 caracteres
"Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
"Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
150 → Formateo a 5 números enteros rellenados con ceros
7887 → Formateo a 7 números enteros rellenados con espacios
20.02 → Formateo a 3 números enteros y 3 números decimales"""

print("--------->>> 1")

print( "{:>20}".format("Hola Mundo") )
print( "{:.3}".format("Hola Mundo") )
print( "{:^20.2}".format("Hola Mundo") )
print( "{:05d}".format(150) )
print( "{:7d}".format(7887) )
print( "{:07.3f}".format(20.02) )

"""3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**
> 3647
** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **
> 0007
  0040
  0600
  3000
Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas 
conversiones entre tipos cadenas, números y viceversa
"""

import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - Número es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        # Aqui va la lógica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i ))

else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: descomposicion.py [0-9999]")