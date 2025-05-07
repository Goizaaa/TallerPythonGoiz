from math import pow
#return suma

# potencia(x:int)-> int:
    #return int(pow(x,2))



if __name__ == '__main__':
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]




    print(f"Numeros originales:{numeros}")
    #print(f"la suma total con la funcion:{suma(numeros)}")
    #potencia=lambda x:x*x se puede ahorrar si en lugar de llamar la funcion potencia,se pone directamente el lambda
    numerosCuadrados =list(map(lambda x:x*x,numeros))
    print(f"Numeros Cuadrados con una funcion:{numerosCuadrados}")