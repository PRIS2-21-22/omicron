#Subprograma para la comprobación de si un poligono es cóncavo o convexo utilizando el algoritmo del corte de oreja
import poligono
import punto
import vector

class Triangulacion():
    #Constructor al que le pasamos un poligono
    def __init__(self,poligono):
        self.poligono = poligono

    def to_string(self):
        self.poligono.to_string()

    #Le pasamos un vertice y nos forma un triangulo con el vertice a su derecha y el de su izquierda
    def triangulo(self,punto):
        tri = list()
        tri.append(self.poligono.puntos[punto-1])
        tri.append(self.poligono.puntos[punto])
        if(punto==len(self.poligono.puntos)-1):
            tri.append(self.poligono.puntos[0])
        else:
            tri.append(self.poligono.puntos[punto+1])
        return poligono.Poligono(tri)

    #Estos tres métodos son para comprobar si un vértice está dentro de un triangulo
    def triangulo_iv(self,triangulo,p2):
        tri = list()
        tri.append(triangulo.puntos[0])
        tri.append(triangulo.puntos[1])
        tri.append(self.poligono.puntos[p2])
        return poligono.Poligono(tri)

    def triangulo_vd(self,triangulo,p2):
        tri = list()
        tri.append(triangulo.puntos[1])
        tri.append(triangulo.puntos[2])
        tri.append(self.poligono.puntos[p2])
        return poligono.Poligono(tri)

    def triangulo_di(self,triangulo,p2):
        tri = list()
        tri.append(triangulo.puntos[2])
        tri.append(triangulo.puntos[0])
        tri.append(self.poligono.puntos[p2])
        return poligono.Poligono(tri)

#Método que nos devuelve el área de un triangulo para poder comprobar su signo
def area_triangulo_signo(a,b,c):
        AB = vector.Vector(p1 = a, p2 = b)
        AC = vector.Vector(p1 = c, p2 = a)
        BC = vector.Vector(p1 = b, p2 = c)
        return (AB.producto_vectorial()+AC.producto_vectorial()+BC.producto_vectorial())/2.0

class main():
    print("CLASE TRIANGULACION")

    #Debería ser convexo
    """v1 = punto.Punto(x=0, y = 0)
    v2 = punto.Punto(x= 1, y = 0)
    v3 = punto.Punto(x=0.5, y = 1)

    triangulo = poligono.Poligono(puntos = [v1,v2,v3])
    triangulacion = Triangulacion(poligono = triangulo)"""

    #Debería ser convexo
    v1 = punto.Punto(x = -2.0, y = -4.0)
    v2 = punto.Punto(x = 6.0, y = -2.0)
    v3 = punto.Punto(x = 7.0, y = 4.0)
    v4 = punto.Punto(x = -8.0, y = 2.0)

    cuadrado = poligono.Poligono(puntos = [v1,v2,v3,v4])
    triangulacion = Triangulacion(poligono = cuadrado)

    #Debería ser convexo
    """v1 = punto.Punto(x = 8.0, y = 2.0)
    v2 = punto.Punto(x = 6.0, y = 10.5)
    v3 = punto.Punto(x = -4.0, y = 6.5)
    v4 = punto.Punto(x = -10.0, y = -8.0)
    v5 = punto.Punto(x = 6.0, y = -4.5)

    pentagono = poligono.Poligono(puntos = [v1,v2,v3,v4,v5])
    triangulacion = Triangulacion(poligono = pentagono)"""

    #Debería ser cóncavo
    """v1 = punto.Punto(x = 12, y = 3)
    v2 = punto.Punto(x = 10, y = 1)
    v3 = punto.Punto(x = 13, y = 1)
    v4 = punto.Punto(x = 14, y = 3)
    v5 = punto.Punto(x = 12, y = 5)
    v6 = punto.Punto(x = 10, y = 5)

    pol_concavo = poligono.Poligono(puntos = [v1,v2,v3,v4,v5,v6])
    triangulacion = Triangulacion(poligono = pol_concavo)"""

    #Debería ser cóncavo
    """v1 = punto.Punto(x = 5, y = 0)
    v2 = punto.Punto(x = 3, y = 3)
    v3 = punto.Punto(x = 0, y = 4)
    v4 = punto.Punto(x = 3, y = 7)
    v5 = punto.Punto(x = 6, y = 3)
    v6 = punto.Punto(x = 10, y = 4)
    v7 = punto.Punto(x = 6, y = 7)
    v8 = punto.Punto(x = 5, y =10)

    pol_concavo = poligono.Poligono(puntos = [v1,v2,v3,v4,v5,v6])
    triangulacion = Triangulacion(poligono = pol_concavo)"""

    print("Nuestro poligono está formado por los puntos: ",end = " ")
    print(triangulacion.poligono.to_string())

    tipo_vector_triangulos = list()
    cont = 0
    eliminados = 1
    res = 0
    while(len(triangulacion.poligono.puntos)>3):
        triangulo = triangulacion.triangulo(punto = cont)
        ivd = area_triangulo_signo(a = triangulo.puntos[0],b = triangulo.puntos[1], c = triangulo.puntos[2])

        if(ivd > 0):
            aux = 0
            for i in range(len(triangulacion.poligono.puntos)-1):
                triangulo_iv = triangulacion.triangulo_iv(triangulo = triangulo, p2 = i)
                triangulo_vd = triangulacion.triangulo_vd(triangulo = triangulo, p2 = i)
                triangulo_di = triangulacion.triangulo_di(triangulo = triangulo, p2 = i)

                iv = area_triangulo_signo(a = triangulo_iv.puntos[0], b = triangulo_iv.puntos[1], c = triangulo_iv.puntos[2])
                vd = area_triangulo_signo(a = triangulo_vd.puntos[0], b = triangulo_vd.puntos[1], c = triangulo_vd.puntos[2])
                di = area_triangulo_signo(a = triangulo_di.puntos[0], b = triangulo_di.puntos[1], c = triangulo_di.puntos[2])

                if(iv > 0 and vd > 0 and di > 0):
                    aux = aux + 1

            if(aux == 0):
                print("Triángulo válido")
                print("Eliminamos el vertice: v",end="")
                print(cont+eliminados)
                tipo_vector_triangulos.append(triangulo)
                triangulacion.poligono.puntos.pop(cont)
                eliminados = eliminados + 1
            else:
                print("Triángulo no válido (tiene un punto intermedio) con el vértice: v",end="")
                print(cont+eliminados)
                res = 1
                break

        else:
            print("Triángulo no válido (ángulo mayor a 180º) con el vértice: v",end="")
            print(cont+eliminados)
            res = 1
            break

    if(res == 0):
        print("Nuestro array de triangulos es:",end=" ")
        tipo_vector_triangulos.append(triangulacion.poligono)
        string = "["
        for i in range(len(tipo_vector_triangulos)):
            if(i!=len(tipo_vector_triangulos)-1):
                string = string + tipo_vector_triangulos[i].to_string() + ", "
            else:
                string = string + tipo_vector_triangulos[i].to_string()
        string = string +"]"
        print(string)
        print("El polígono es convexo")
    else:
        print("El polígono es cóncavo")