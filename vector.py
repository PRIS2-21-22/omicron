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
        return math.sqrt(math.pow(self.cordX,2) + math.pow(self.cordY,2))

    #Cálculo del producto vectorial
    def productoVectorial(self):
        return self.p1.cordX()*self.p2.cordY() - self.p1.cordY()*self.p2.cordX()
