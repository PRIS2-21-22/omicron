import punto
import vector

class Poligono():
    #Constructor de la clase Poligono
    def __init__(self,puntos):
        self.lados = len(puntos)
        self.puntos = puntos

#Ejemplo creación de un poligono
class main():
    cuadrado = Poligono(puntos = [(0,0),(1,1),(1,0),(0,1)])
    print(cuadrado.lados)