MAX = 100

class tipo_poligono():
    n: int
    v: tipo_v_p

class tipo_v_p(): 
    vector[1..MAX] type tipo_punto2d

class tipo_punto2d():
        x,y: float

class tipo_triangulacion:
        n: int
        t: tipo_v_t

class tipo_v_t():
     vector[1..MAX] de tipo_tri

class tipo_tri():
     vector[1..3] de tipo_punto2d

def triangulacion(tipo_poligono poligono, tipo_v_p vectores):

    return 