#!/usr/bin/python3

# from evaluate import expresiones

# RELATIONAL OPERATORS

"""
En una lista llamada expresiones encontramos diferentes operaciones relacionales, ¿podrías determinar 
mentalmente el resultado de cada expresión y almacenarlo en una nueva lista llamada resultados? Esta l
ista debe contener únicamente valores lógicos True y False. Por ejemplo, supongamos esta lista:

expresiones = [1 == 1, 1 < 0]
La respuesta que se espera que escribas es:

resultados = [True, False]
Correspondiendo True al resultado de 1==1 y False al de 1<0,  es decir, los resultados deben concordar 
con la posición de las expresiones, siendo resultados[0] la respuesta a la expresión expresiones[0].

La lista de expresiones que debes calcular mentalment es la siguiente (se importará automáticamente 
durante la comprobación de la solución):

expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]
Sugerencia: ¿Eres muy perezos@ como para pensar? ¡Deja que Python calcule las expresiones por ti!
"""

resultados = [False,True,True,True,True]

# LOGIC OPERATORS

"""
Expresiones anidadas
A partir de dos variables nombre y edad crea una variable expresion que almacene si se 
cumplen TODAS las siguientes condiciones encadenando operadores lógicos en una sola línea:

Que nombre sea diferente de cuatro asteriscos.

Que edad sea mayor que 10 y a su vez menor que 18.

Que la longitud del nombre sea mayor o igual que 3 pero a la vez menor que 10.

Nota: Utiliza paréntesis para encadenar diferentes conjuntos de expresiones lógicas entre ellas.

Por cierto, en este ejercicio edad y nombre se cargarán durante la solución así que no sabes qué 
contienen, no les des ningún valor manualmente o el test fallará.
"""

nombre = "****"
edad = 22

expresion = (nombre != "****") and (10 < edad < 18) and (3 <= len(nombre) < 10)

print(expresion) # False