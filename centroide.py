import poligono
import punto

class Centroide():
    #Constructor al que le pasamos un poligono
    def __init__(self,poligono):
        self.poligono = poligono

    #Método que nos calcula el área de un polígono
    def area(self):
        sum = 0
        for i in range(self.poligono.lados):
            if(i != self.poligono.lados-1):
                sum = sum + (self.poligono.puntos[i].get_x()*self.poligono.puntos[i+1].get_y() - self.poligono.puntos[i+1].get_x()*self.poligono.puntos[i].get_y())
            else:
                sum = sum + (self.poligono.puntos[i].get_x()*self.poligono.puntos[0].get_y() - self.poligono.puntos[0].get_x()*self.poligono.puntos[i].get_y())
        return sum/2

    #Método que nos calcula la abscisa(x) del centroide
    def xcent(self,area):
        sum = 0
        for i in range(self.poligono.lados):
            if(i != self.poligono.lados-1):
                sum = sum + (self.poligono.puntos[i+1].get_x() + self.poligono.puntos[i].get_x())*(self.poligono.puntos[i].get_x()*self.poligono.puntos[i+1].get_y() - self.poligono.puntos[i+1].get_x()*self.poligono.puntos[i].get_y())
            else:
                sum = sum + (self.poligono.puntos[0].get_x() + self.poligono.puntos[i].get_x())*(self.poligono.puntos[i].get_x()*self.poligono.puntos[0].get_y() - self.poligono.puntos[0].get_x()*self.poligono.puntos[i].get_y())
        return sum/(6*area)

    #Método que nos calcula la ordenada(y) del centroide
    def ycent(self,area):
        sum = 0
        for i in range(self.poligono.lados):
            if(i != self.poligono.lados-1):
                sum = sum + (self.poligono.puntos[i+1].get_y() + self.poligono.puntos[i].get_y())*(self.poligono.puntos[i].get_x()*self.poligono.puntos[i+1].get_y() - self.poligono.puntos[i+1].get_x()*self.poligono.puntos[i].get_y())
            else:
                sum = sum + (self.poligono.puntos[0].get_y() + self.poligono.puntos[i].get_y())*(self.poligono.puntos[i].get_x()*self.poligono.puntos[0].get_y() - self.poligono.puntos[0].get_x()*self.poligono.puntos[i].get_y())
        return sum/(6*area)

class main():
    print("CLASE CENTROIDE")
    lados = 0
    while(lados < 3):
        print("Introduzca el número de lados (ha de ser mayor o igual a 3):",end=" ")
        lados = int(input())
    
    puntos = list()
    for i in range(lados):
        print(f"Introduzca la abscisa(x) del punto {i+1}")
        x = int(input())
        print(f"Introduzca la ordenada(y) del punto {i+1}")
        y = int(input())
        punt = punto.Punto(x = x, y = y)
        puntos.append(punt)
    
    poligono = poligono.Poligono(puntos = puntos)
    print(f"El poligono es: {poligono.toString()}")

    centroide = Centroide(poligono = poligono)
    area = centroide.area()
    xcent = centroide.xcent(area = area)
    ycent = centroide.ycent(area = area)

    puntoCentroide = punto.Punto(x = xcent, y = ycent)
    print(f"El centroide del poligono introducido es: {puntoCentroide.toString()}")