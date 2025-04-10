class Auto:
    marca="Honda" #ATERIBUTOS DE LA CLASE AUTO
    modelo=1000
    placa="PCH-96-04"

if __name__ == '__main__':
    taxi=Auto()#es instancias de la clase archivo
    miauto=Auto()

    print(taxi.placa)#se involucran los atrubutos
    miauto.placa="TCV-963-12"
    print(miauto.placa)