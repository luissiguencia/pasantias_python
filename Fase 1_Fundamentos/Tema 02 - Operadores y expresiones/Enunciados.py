"""
1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero
"""

# Completa el ejercicio aquí
n1 = float( input("Introduce el primer número: ") )
n2 = float( input("Introduce el segundo número: ") )

print("¿Son iguales? ", n1 == n2)
print("¿Son diferentes?", n1 != n2)
print("¿El primero es mayor que el segundo?", n1 > n2)
print("¿El segundo es mayor o igual que el primero?", n1 <= n2)

"""
2) Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):
"""

cadena = input("Escribe una cadena: ")
print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?", len(cadena) >= 3 and len(cadena) < 10 )

"""
3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que sea un número entero)
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""

numero_magico = 12345679
numero_usuario = int(input("Introduce un número del 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print("El número mágico es:", numero_magico)