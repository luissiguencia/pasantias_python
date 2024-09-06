#!/usr/bin/python3

courses = {}

def validate_dni(dni):
    if len(dni) == 10 and dni.isdigit():
        return True
    return False

# def validate_course(course_name):
#     if course_name.upper() in courses:
#         return True
#     return False

print("---->> BIENVENIDO")

while True:
    print("[+] ELIGE UNA OPCION")
    print("--->> 1. INGRESAR UN CURSO")
    print("--->> 2. INGRESAR UN ESTUDIANTE")
    print("--->> 3. V3ISUALIZAR INFORMACION")
    print("--->> 4. SALIR")
    
    main_menu = input("Opcion: ")

    match main_menu:
        case "1":
            while True:
                print("[+] ELIGE UNA OPCION")
                print("--->> 1. INGRESAR UN CURSO")
                print("--->> 2. REGRESAR")

                menu_course = input("Opcion: ")

                match menu_course:
                    case "1":
                        course = input("Ingresa el curso: ")
                        if course in courses:
                            print(f"[ALERTA] {course} ya existe")
                        else:
                            courses[course.upper()] = []
                            print(f"Curso {course} agregado exitosamente")
                            print(courses)
                    case "2":
                        break
                    case _:
                        print("!!! Escoge una opcion valida")

        case "2":            
            if bool(courses):
                while True:
                    print("[+] ELIGE UNA OPCION")
                    print("--->> 1. INGRESAR ALUMNO")
                    print("--->> 2. REGRESAR")
    
                    menu_alumno = input("Opcion: ")
    
                    match menu_alumno:
                        case "1":
                            dni = input("Cedula: ")
                            while True:
                                if not validate_dni(dni):
                                    print(f"<--- {dni} no es una cedula")
                                    dni = input("Cedula: ")
                                else:
                                    break
                                
                            name = input("Nombres y Apellidos: ")
    
                            age = input("Edad: ")
                            while True:
                                if not age.isdigit():
                                    print(f"<--- {age} no es una edad")
                                    age = input("Edad: ")
                                else:
                                    break
                                
                            address = input("Direccion: ")
                            student = [dni, name.upper(), age, address.upper()]
    
                            course_name = ""
    
                            while True:
                                course_name = input("Elige el curso: ")
                                if course_name.upper() not in courses:
                                    print("Curso no existente")
                                else:
                                    courses[course_name].append(student)
                                    print(courses)
                                    break
                        case "2":
                            break
                        case _:
                            print("!!! Escoge una opcion valida")
            else:
                print("<<----NO HAY CURSOS")

        case "3":
            while True:
                print("[+] ELIGE UNA OPCION")
                print("--->> 1. MOSTRAR CURSOS")
                print("--->> 2. MOSTRAR ESTUDIANTES")
                print("--->> 4. SALIR")

                menu_view = input("Opcion: ")

                if len(courses) != 0:
                    match menu_view:
                        case "1":
                            for n, course in enumerate(courses.keys(), start=1):
                                print(f"\t{n}. {course}")
                        case "2":
                            for curso, students in courses.items():
                                print(f"Curso: {curso}")
                                for datos in students:
                                    dni, name, age, address = datos
                                    print("{:<20} {:<15} {:<10} {:<30}".format("Estudiante", "Cédula", "Edad", "Dirección"))
                                    print("{:<20} {:<15} {:<10} {:<30}".format(name, dni, age, address))
                                print()
                        case "4":
                            break
                        case _:
                            print("!!! Escoge una opcion valida")
                
        case "4":
            print("ADIOS")
            break
        case _:
            print("!!! Escoge una opcion valida")



