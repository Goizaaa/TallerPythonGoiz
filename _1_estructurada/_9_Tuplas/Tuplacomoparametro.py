


def calcular_a(rectangulo:tuple [int, int ])-> int:
    largo, ancho =rectangulo
    return largo *ancho

def cuadrado(rectangulo:tuple[int, int])->int:
    largo, ancho=rectangulo
    largo, largo *largo
    ancho=ancho+ancho
    return (largo, ancho)



if __name__ == '__main__':

    dimensiones = (10,5)


    #llamar a la funciones con la tubla
    area =calcular_a(dimensiones)
    print(f"el area del retangulo es:{area} mts. cuadrados")

    largo,ancho= cuadrado((5,3))
    print(f"el largo es {largo} y ancho {ancho}")