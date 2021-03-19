import poligono
import punto

class Triangulacion():
    def __init__(self,poligono):
        self.poligono = poligono
    
    def toString(self):
        self.poligono.toString()

    def triangulo(self):
        tri = list()
        tri.append(self.poligono.puntos[-1])
        tri.append(self.poligono.puntos[0])
        tri.append(self.poligono.puntos[1])
        return poligono.Poligono(tri)

    def area_triangulo_signo(self,a,b,c):
    AB = self.vector(p1 = a, p2 = b)
    AC = self.vector(p1 = a, p2 = c)
    BC = self.vector(p1 = b, p2 = c)
    return (self.AB.productoVectorial+self.AC.productoVectorial+self.BC.productoVectorial)/2.0
 
class main():
    A = punto.Punto(x = 0, y = 0)
    B = punto.Punto(x = 0, y = 1)
    C = punto.Punto(x = 1, y = 1)
    D = punto.Punto(x = 1, y = 0)

    cuadrado = poligono.Poligono(puntos = [A,B,C,D])
    triangulacion = Triangulacion(poligono = cuadrado)
    triangulacion.toString()

    triangulo = triangulacion.triangulo()
    triangulo.toString()

    ivd = triangulacion.area_triangulo_signo(a = triangulo.puntos[0],b = triangulo.puntos[1], c = triangulo.puntos[2])
    
    if( <= 0 ||)


'''class Cuadrado():
    A = tipo_punto2d(1,1)
    B = tipo_punto2d(2,2)
    C = tipo_punto2d(3,3)
    D = tipo_punto2d(0,0)
    tipo_v_p.vector.append(A)
    tipo_v_p.vector.append(B)
    tipo_v_p.vector.append(C)
    tipo_v_p.vector.append(D)
    puntos = tipo_v_p.vector
    cuadrado = tipo_poligono(4,puntos)
    return cuadrado

class triangulacion(poligono):
    for i in poligono.n:
        A = tipo_tri.vector.append(poligono.vector[i-1])
        B = tipo_tri.vector.append(poligono.vector[i])
        C = tipo_tri.vector.append(poligono.vector[i+1])
        if(area_triangulo_signo(A,B,C)>0):
            poligono.vector[i] = 0
            tipo_triangulacion.vector.append(tipo_tri.vector)
        else:
            poligono.n++
    return tipo_triangulacion 
    

class main():
    cuadrado = Cuadrado()
    triangulacion(cuadrado)'''

    
