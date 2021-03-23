import math
import punto

class Vector():
    #Constructor de la clase Vector
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    #Calculo de las coordenadas de X
    def cordX(self):
        return self.p2.get_x() - self.p1.get_x()

    #Cálculo de las coordenadas de Y
    def cordY(self):
        return self.p2.get_y() - self.p1.get_y()

    #Calculo del módulo de un vector
    def modulo(self):
        return math.sqrt(math.pow(self.cordX(),2) + math.pow(self.cordY(),2))

    #Cálculo del producto vectorial
    def productoVectorial(self):
        return self.p1.get_x()*self.p2.get_y() - self.p1.get_y()*self.p2.get_x()

class main():
    print("CLASE VECTOR")
    punto1 = punto.Punto(x = 0.15, y = 0.25)
    punto2 = punto.Punto(x = 0.0, y = -1.0)
    v = Vector(p1 = punto1, p2 = punto2)
    print("Coordenada x = ",end=" ")
    print(v.cordX())
    print("Coordenada y = ",end=" ")
    print(v.cordY())
    print("Modulo = ",end=" ")
    print(v.modulo())
    print("Producto vectorial = ",end=" ")
    print(v.productoVectorial())
