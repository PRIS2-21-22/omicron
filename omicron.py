MIN = 1
MAX = 100
maxTipoTri = 3

class tipo_v_p(): 
    vector = [MIN for x in range(MAX)]

class tipo_poligono():
    n: int
    v: tipo_v_p

class tipo_punto2d():
        x: float
        y: float

class tipo_v_t():
     vector = [MIN for x in range(MAX)]

class tipo_triangulacion:
        n: int
        t: tipo_v_t

class tipo_tri():
     vector = [MIN for x in range(maxTipoTri)]

def triangulacion(tipo_poligono, tipo_v_p ):

    return 