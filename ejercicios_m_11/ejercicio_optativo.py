import math

class Punto:
    
    #Función para instanciar el punto x y punto y
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #Función para mostrar en el formato definido cada variable en una sola cadena
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    #Función donde por distintas condiciones se mostrará a que cuadrante pertenece las variables
    #Haciendo alusión a un plano cartesiano
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
    
    #Función para calcular el vector entre la primera coordenada y el segundo punto que se hará referencia
    #En format usamos la fórmula con cada variable para obtener el resultado y mostrarlo al imprimir por pantalla
    def vector(self,p):
        print("El vector resultante entre {} y {} es ({}, {})".format(self,p, p.x - self.x, p.y - self.y))
    
    def distancia(self,p):
       d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
       print("La distancia resultante entre {} y {} es {}".format(self,d,p))

class Rectangulo:
    def __init__(self,pInicial=Punto(),pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
    def base(self):
        self.base= abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format(self.base))
    
    def altura(self):
        self.altura= abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format(self.altura))
    
    def area(self):
        self.base= abs(self.pFinal.x - self.pInicial.x)
        self.altura= abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        
        print("EL área del rectángulo es {}".format(self.area))
    