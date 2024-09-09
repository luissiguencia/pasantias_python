#Se ha creado una función donde al realizarse una división entre 0 nos devolverá una excepción para
#que no se detenga la ejecución del programa
def dividir(a, b):
    try:
        return a/b
    except:
        print("No se puede dividir entre cero")
    