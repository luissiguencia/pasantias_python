from collections import deque

cursos = ["Primero A", "Primero B", "Segundo A","Segundo B", "Tercero A", "Cuarto A"]
datos_estudiante ={}
estudiante=[]

opcion=0
while opcion!=5:
    
    print("****¿Qué deseas hacer?****")
    print("1)Registrar Estudiante\n"
      "2)Ver todos los estudiantes\n"
      "3)Ver todos los cursos\n"
      "4)Ver estudiantes por curso\n"
      "5)SALIR")
    opcion=int(input("Escribe una opción: "))

    match opcion:

        case 1:
            
            cedula=input("Ingrese la cédula del estudiante: ")
            if len(cedula)==10:
               datos_estudiante["Cédula"]= cedula

               if len(cedula)!=0:
                    nombres=input("Ingrese los nombres completos del estudiante: ")
                    if len(nombres)>0:
                       datos_estudiante["Nombres"] = nombres
                       
                       if len(nombres)!=0:
                         edad=int(input("Ingrese la edad del estudiante: "))
                         if edad>0:
                           datos_estudiante["Edad"] = edad
                           
                           direccion=input("Ingrese la dirección de domicilio: ")
                           if len(direccion)>0:
                            datos_estudiante["Direccion"]=direccion
                            
                            while(True):
                                curso= input("Ingrese el Curso al que se matriculará el estudiante: ")
                                try:
                                    if cursos.index(curso):
                                      datos_estudiante["Curso"]=curso 
                                    break
                                except:
                                    print("Curso ingresado no existe, vuelva a intentar")
                    else:
                       print("Datos inválidos, ingrese nuevamente")
                       
            else:
                print("La cédula debe contener 10 dígitos")
            
            estudiante.append(datos_estudiante)
            
        case 2:
            print("*Lista de Estudiantes*")
            for est in estudiante:
                print(est)
            print()
            
        case 3:
            print("*Lista de Cursos*")     
            for c in cursos:
                print(c)
            print()
      
        case 4:
            while(True):
                print("Estudiantes por curso")
                curso= input("Ingrese el curso del que desea visualizar los estudiantes registrados")
                               
                try:
                    if estudiante.index(curso):
                       for est in estudiante:
                         print(est)         
                    break
                except:
                    print("No hay estudiantes registrados en este curso")  
        case 5:
          print("Saliendo del sistema...Vuelva pronto")
        
        



