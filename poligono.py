#Esta clase se encarga de la representación de un poligono a través de un array de puntos
import punto

class Poligono():
    #Constructor de la clase Poligono
    def __init__(self,puntos):
        self.lados = len(puntos)
        self.puntos = puntos
    
    def to_string(self):
        string = "["
        for i in range(len(self.puntos)):
            if(i!=len(self.puntos)-1):
                string = string + self.puntos[i].to_string() + ", "
            else:
                string = string + self.puntos[i].to_string()
        string = string + "]"
        return string

#Ejemplo creación de un poligono
class main():
    print("CLASE POLIGONO")
    A = punto.Punto(x = 0, y = 0)
    B = punto.Punto(x = 0, y = 1)
    C = punto.Punto(x = 1, y = 0)
    D = punto.Punto(x = 1, y = 1)
    cuadrado = Poligono(puntos = [A,B,C,C])
    print("Los puntos del poligono \"cuadrado\" son:", end = " ")
    print(cuadrado.to_string())

    cuadrado.puntos.pop(0)
    print("Eliminaremos el primer punto:", end = " ")
    print(cuadrado.to_string())

    cuadrado.puntos.pop(0)
    print("Probamos a eliminar otra vez el primer punto:", end = " ")
    print(cuadrado.to_string())
    print()