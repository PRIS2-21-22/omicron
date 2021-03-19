import punto
import vector

class Poligono():
    #Constructor de la clase Poligono
    def __init__(self,puntos):
        self.lados = len(puntos)
        self.puntos = puntos

    def toString(self):
        print(self.lados)
        print("[",end="")
        for i in range(self.lados):
            self.puntos[i].toString()
        print("]")

#Ejemplo creación de un poligono
'''class main():
    A = punto.Punto(x = 0, y = 0)
    B = punto.Punto(x = 0, y = 1)
    C = punto.Punto(x = 1, y = 0)
    D = punto.Punto(x = 1, y = 1)
    cuadrado = Poligono(puntos = [A,D,C,B])
    cuadrado.toString()'''