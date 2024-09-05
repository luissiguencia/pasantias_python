# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# Completa el ejercicio
grupo.add('Ana')
grupo.add('Ramón')
grupo.add('Marta')
grupo.add('Eric')
grupo.add('David')
grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")
print(grupo)

#Alternativa optimizada con bucles
for nombre in ['Ana','Ramón','Marta','Eric','David']:
    grupo.add(nombre)

for nombre in ['Mario','Miguel','Ramón']:
    grupo.remove(nombre)