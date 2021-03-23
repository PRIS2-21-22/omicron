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
        return math.sqrt(math.pow(self.cordX(),2) + math.pow(self.cordY(),2))

    #Cálculo del producto vectorial
    def productoVectorial(self):
        return self.p1.get_x()*self.p2.get_y() - self.p1.get_y()*self.p2.get_x()

    #Cálculo de la ecuación de la recta dados dos puntos
    def ecuacionRecta(self):
        division = ((self.p2.get_y()-self.p1.get_y())/(self.p2.get_x()-self.p1.get_x()))
        return f"y = {division}*(x-{self.p1.get_x()}) + {self.p1.get_y()}"

    #Ecuación de la recta dada una pendiente y la ordenada de origen
    def ecuacionRecta2(self,pendiente,ordenada):
        return f"y = {pendiente}*x + {ordenada}"

    #Ecuación de la recta dada una pendiente y un punto de esta
    def ecuacionRecta3(self,pendiente,punto):
        return f"y = {pendiente}*(x-{punto.get_x()}) + {punto.get_y()}"

    #Ecuación de la recta dados los coeficientes del polinomio de su representación explícita
    def ecuacionRecta4(self,a,b,c):
        return f"{a}*x + {b}*y + {c} = 0"

    def ecuacionRecta5(self, x0):
        return f"x = {x0}"

    def ecuacionRecta6(self, y0):
        return f"y = {y0}"

def representacionImplicita(linea):
    items = linea.split(' + ')
    ab = items[0].split(' = ')
    a = ab[0]
    b = ab[1]
    c = items[1]
    return f"{b} - {a} + {c} = 0"
    
def interseccion(linea1,linea2):
    items = linea1.split(" = ")
    items2 = linea2.split(" = ")
    pendiente = items[1].split("*")
    pendiente2 = items2[1].split("*")
    p1 = pendiente[0]
    p2 = pendiente2[0]
    if(p1 == p2):
        return "Líneas paralelas/coincidentes"
    else:
        return "Líneas secantes"

class main():
    print("CLASE VECTOR")
    punto1 = punto.Punto(x = 0.15, y = 0.25)
    punto2 = punto.Punto(x = 0.0, y = -1.0)
    v = Vector(p1 = punto1, p2 = punto2)
    print(f"Coordenada x = {v.cordX()}")
    print(f"Coordenada y = {v.cordY()}")
    print(f"Modulo = {v.modulo()}")
    print(f"Producto vectorial = {v.productoVectorial()}")
    print(f"Ecuacion de la recta: {v.ecuacionRecta()}")
    m = 5
    b = 4
    print(f"Dados una pendiente {m} y una ordenada {b}, la ecuación de la recta es: {v.ecuacionRecta2(pendiente = m, ordenada = b)}")
    print(f"Dada una pendiente {m} y un punto {v.p1.toString()}, la ecuación de la recta es: {v.ecuacionRecta3(pendiente = m, punto = v.p1)}")
    a = 1
    b = 2
    c = 0
    print(f"Dados los coeficientes {a}, {b} y {c}, la ecuación de la recta es: {v.ecuacionRecta4(a = a, b = b , c = c)}")
    print(f"Dada la abscisa {v.p1.get_x()}, la ecuación de la recta (vertical) es: {v.ecuacionRecta5(x0 = v.p1.get_x())}")
    print(f"Dada la ordenada {v.p1.get_y()}, la ecuación de la recta (horizontal) es: {v.ecuacionRecta6(y0 = v.p1.get_y())}")

    print(f"La recta {v.ecuacionRecta()} en forma implícita sería: {representacionImplicita(linea = v.ecuacionRecta())}")
    print(f"La recta {v.ecuacionRecta2(pendiente = m, ordenada = b)} en forma implícita sería: {representacionImplicita(linea = v.ecuacionRecta2(pendiente = m, ordenada = b))}")
    print(f"La recta {v.ecuacionRecta3(pendiente = m, punto = v.p1)} en forma implícita sería: {representacionImplicita(linea = v.ecuacionRecta3(pendiente = m, punto = v.p1))}")

    p3 = punto.Punto(x = 4, y = 4)
    p4 = punto.Punto(x = 5, y = 5)
    v2 = Vector(p1 = p3, p2 = p4)

    print(f"Las rectas ({v2.ecuacionRecta()}) y ({v.ecuacionRecta()}) son: {interseccion(linea1 = v2.ecuacionRecta(), linea2 = v.ecuacionRecta())} ")

    p5 = punto.Punto(x = 2, y = 2)
    p6 = punto.Punto(x = 2.5, y = 2.5)
    v3 = Vector(p1 = p5, p2 = p6)

    print(f"Las rectas ({v2.ecuacionRecta()}) y ({v3.ecuacionRecta()}) son: {interseccion(linea1 = v2.ecuacionRecta(), linea2 = v3.ecuacionRecta())} ")

