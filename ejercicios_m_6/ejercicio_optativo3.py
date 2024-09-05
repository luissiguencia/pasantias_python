from collections import deque
tareas=[
    [6,'Distribución'],
    [2,'Diseño'],
    [1,'Concepción'],
    [7,'Mantenimiento'],
    [4,'Producción'],
    [3,'Planificación'],
    [5,'Pruebas']
]

print("--Tareas desordenadas--")
for tarea in tareas:
    print(tarea[0],tarea[1])

tareas.sort()

cola=deque()
for tarea in tareas:
    cola.append(tarea[1]) #Agregamos en la variable cola cada elemento ubicado en el índice 1
                          #Así añadirá solo los nombres

print("\n--Tareas ordenadas--") 
for tarea in cola:       #Ahora recorremos con un for la cola creada
    print(tarea)
