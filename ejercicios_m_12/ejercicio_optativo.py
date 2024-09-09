#Código de ejemplo sin instaciar una super clase para heredar los atributos
#de la primera clase
# class Vehiculo():
    
#     def __init__(self,color,ruedas):
#         self.color = color
#         self.ruedas =ruedas
    
#     def __str__(self):
#         return "color {}, {} ruedas".format(self.color, self.ruedas)

# class Coche(Vehiculo):
    
#     def __init__(self, color, ruedas, velocidad, cilindrada):
#          self.color = color
#          self.ruedas = ruedas
#          self.velocidad = velocidad
#          self.cilindrada = cilindrada
    
#     def __str__(self):
#         return "color {}, {} k/h, {} ruedas,{} cc".format(self.color,self.velocidad,self.ruedas,self.cilindrada)


class Vehiculo():
    
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas =ruedas
    
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
         super().__init__(color, ruedas) #Se usa super() en lugar de la clase Vehiculo
         self.velocidad = velocidad
         self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__()+", {} k/h, {} cc".format(self.velocidad,self.cilindrada)

#c = Coche("azul",4,150,1200)
#print(c)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
         super().__init__(color, ruedas,velocidad,cilindrada)
         self.carga = carga
    
    def __str__(self):
        return super().__str__()+", {} kg de carga".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
         super().__init__(color, ruedas)
         self.tipo = tipo
    
    def __str__(self):
        return super().__str__()+", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas,tipo,velocidad,cilindrada):
         super().__init__(color, ruedas,tipo)
         self.velocidad = velocidad
         self.cilindrada =cilindrada
    
    def __str__(self):
        return super().__str__()+", {} k/h, {} cc".format(self.velocidad, self.cilindrada)

vehiculos=[
    Coche("Rojo",4,150,1200),
    Camioneta("Azul",4,100,1300,1500),
    Bicicleta("Amarillo", 2, "Urbana"),
    Motocicleta("Negro", 2, "Deportiva",100,900)
]

# def catalogar(lista):
#     for v in lista:
#         print("{} {}".format(type(v).__name__,v))

# catalogar(vehiculos)

def catalogar(lista, ruedas=None):
    if ruedas != None:
        contador =0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador+=1
        print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
        print("*********************************************")
    for v in lista:
        if ruedas == None:
         print("{} {}".format(type(v).__name__,v))
        else:
            if v.ruedas == ruedas:
                print("{} {}".format(type(v).__name__,v))
                
catalogar(vehiculos,4)