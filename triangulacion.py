import poligono
import punto
import vector

class Triangulacion():
    def __init__(self,poligono):
        self.poligono = poligono
    
    def toString(self):
        self.poligono.toString()

    def triangulo(self,punto):
        tri = list()
        tri.append(self.poligono.puntos[punto-1])
        tri.append(self.poligono.puntos[punto])
        if(punto+1>len(self.poligono.puntos)):
            tri.append(self.poligono.puntos[0])
        else:
            tri.append(self.poligono.puntos[punto+1])
        return poligono.Poligono(tri)

def area_triangulo_signo(a,b,c):
        AB = vector.Vector(p1 = a, p2 = b)
        print("AB = ",end=" ")
        print(AB.productoVectorial())
        AC = vector.Vector(p1 = a, p2 = c)
        print("AC = ",end=" ")
        print(AC.productoVectorial())
        BC = vector.Vector(p1 = b, p2 = c)
        print("BC = ",end=" ")
        print(BC.productoVectorial())
        print((AB.productoVectorial()+AC.productoVectorial()+BC.productoVectorial())/2.0)
        return (AB.productoVectorial()+AC.productoVectorial()+BC.productoVectorial())/2.0
 
class main():
    print("CLASE TRIANGULACION")
     
    '''v1 = punto.Punto(x = -2.0, y = -4.0)
    v2 = punto.Punto(x = 6.0, y = -2.0)
    v3 = punto.Punto(x = 7.0, y = 4.0)
    v4 = punto.Punto(x = -8.0, y = 2.0)

    cuadrado = poligono.Poligono(puntos = [v1,v2,v3,v4])'''

    v1 = punto.Punto(x = 0.0, y = 0.0)
    v2 = punto.Punto(x = 0.0, y = 1.0)
    v3 = punto.Punto(x = 1.0, y = 1.0)
    v4 = punto.Punto(x = 1.0, y = 0.0)
    v5 = punto.Punto(x = -0.5, y = 0.5)

    pentagono = poligono.Poligono(puntos = [v1,v2,v3,v4,v5])
    '''v1 = punto.Punto(x = 0, y = 0)
    v2 = punto.Punto(x = 1, y = 1)
    v3 = punto.Punto(x = 2, y = 0.25)
    v4 = punto.Punto(x = 1.50, y = 0.30)
    v5 = punto.Punto(x = 1.50, y = 3)
    v6 = punto.Punto(x = 1.35, y = 3.25)
    v7 = punto.Punto(x = 1.15, y = 1.25)
    v8 = punto.Punto(x = 0.85, y = 3.50)
    v9 = punto.Punto(x = -0.50, y = 3.15)
    v10 = punto.Punto(x = 0.60, y = 2.75)
    v11 = punto.Punto(x = -1, y = 1.30)

    pol = poligono.Poligono(puntos = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11])'''
    triangulacion = Triangulacion(poligono = pentagono)
    print("Nuestro poligono está formado por los puntos: ",end = " ")
    print(triangulacion.poligono.toString())

    tipo_vector_triangulos = list()
    cont = 0
    while(len(triangulacion.poligono.puntos)>3):
        triangulo = triangulacion.triangulo(punto = cont)
        ivd = area_triangulo_signo(a = triangulo.puntos[0],b = triangulo.puntos[1], c = triangulo.puntos[2])
    
        if(ivd > 0):
            print("Eliminamos el vertice:",end=" ")
            print(triangulacion.poligono.puntos[cont].toString())
            tipo_vector_triangulos.append(triangulo)
            triangulacion.poligono.puntos.pop(cont)
        else:
            if(cont == len(triangulacion.poligono.puntos)):
                cont = 0
            else:
                cont = cont+1
    
    print("Nuestro array de triangulos es:",end=" ")
    tipo_vector_triangulos.append(triangulacion.poligono)
    string = "["
    for i in range(len(tipo_vector_triangulos)):
        if(i!=len(tipo_vector_triangulos)-1):
            string = string + tipo_vector_triangulos[i].toString() + ", "
        else:
            string = string + tipo_vector_triangulos[i].toString()
    string = string +"]"
    print(string)


    
