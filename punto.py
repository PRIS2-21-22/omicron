#Esta clase se encarga de la representación de un punto en un espacio de 2D
class Punto():
    #Constructor de la clase Punto
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_coord(self,cordX, cordY):
        self.x = cordX
        self.y = cordY

    def to_string(self):
        return "("+str(self.x)+","+str(self.y)+")"


class main():
    print("CLASE PUNTO")
    punto = Punto(x = 0, y = 0)
    print("El punto introducido es:", end = " ")
    print(punto.to_string())
    print()
    
