"""
Errores
En la función del ejercicio hay un fallo potencial, averigua cuando sucede y retorna 
el valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal 
de la función.

Pista: Valor indeterminado.
"""

def dividir(a, b):
    if(b==0):
        return None
    return a/b
    
print(dividir(0, 0))


"""
Excepciones
Tomando la solución al anterior ejercicio, en lugar de devolver None al dividir 
entre cero, debes capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje 
No se puede dividir entre cero si falla el código.
"""

def divide(a, b):
    try:
        return a / b
    except:
        print("No se puede dividir entre cero si falla el código.")
    
print(divide(4, 0))