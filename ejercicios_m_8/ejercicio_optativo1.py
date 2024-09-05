#Formatear los valores para mostrar el resultado requerido
print("{:>20}".format("Hola Mundo")) #Alineamiento a la derecha con 20 caracteres
print("{:.3}".format("Hola Mundo")) #Truncamiento en el cuarto caracter
print("{:^20.1}".format("Hola Mundo")) #Alineado al centro con 20 caracteres y truncado en el segundo caracter
print("{:05d}".format(150)) #Rellenado con 0 a la izquierda alineado a 5 dígitos
print("{:7d}".format(7887)) #Rellenado con espacios y alineado a 7 dígitos
print("{:07.3f}".format(20.02))