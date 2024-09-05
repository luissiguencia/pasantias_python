#Ejercicio 1
n1=float(input("Escribe un número: "))
n2=float(input("Escribe otro número: "))
print("****¿Qué deseas hacer?****")
print("1)Suma\n"
      "2)Resta\n"
      "3)Multiplicación")
opcion=input("Escribe una opción: ")

match opcion:
    case "1":
        print("La suma entre",n1,"+",n2," es:",n1+n2)
    case "2":
        print("La resta entre",n1,"-",n2," es:",n1-n2)
    case "3":
        print("La multiplicación entre",n1,"x",n2," es:",n1*n2)
    case _:
        print("*Operación finalizada*")





