MAX = 100

class tipo_v_p(): 
    vector = [1 for i in range(MAX)]

class tipo_poligono():
    n: int
    v: tipo_v_p

class tipo_punto2d():
        x: float
        y: float

class tipo_v_t():
     vector = [1 for i in range(MAX)]

class tipo_triangulacion:
        n: int
        t: tipo_v_t

class tipo_tri():
     vector = [1 for i in range(3)]

def triangulacion(tipo_poligono, tipo_v_p ):

    return 