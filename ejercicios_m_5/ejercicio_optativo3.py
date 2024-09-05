#Ejercicio 3
numero=100
suma=0
#Se deben sumar todos los números pares hasta el 100
#Forma 1
for n in range(numero+1):
    if(n % 2==0):
        suma+=n

print(suma)

#Forma 2
suma2=sum(range(0,101,2))
print(suma2)