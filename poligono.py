import punto
import vector

class Poligono():
    #Constructor de la clase Poligono
    def __init__(self,puntos):
        self.lados = len(puntos)
        self.puntos = puntos

    def toString(self):
        string = "["
        for i in range(len(self.puntos)):
            if(i!=len(self.puntos)-1):
                string = string + self.puntos[i].toString() + ", "
            else:
                string = string + self.puntos[i].toString()
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
    print(cuadrado.toString())

    cuadrado.puntos.pop(0)
    print("Eliminaremos el primer punto:", end = " ")
    print(cuadrado.toString())

    cuadrado.puntos.pop(0)
    print("Probamos a eliminar otra vez el primer punto:", end = " ")
    print(cuadrado.toString())
    print()