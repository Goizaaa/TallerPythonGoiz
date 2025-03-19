import statistics as webo
#def suma(a:int,b:int):

 #   print(f"la suma de {a}+{b} es {a+b} ")

def suma(a: int, b= None,c=None):
    if b is None:
        print(f"la suma de {a} es {a} ")
    else:

        if c is None:
            print(f"la suma de {a}+{b} es {a + b} ")
        else:
            print(f"la suma de {a}+{b}+{c} es {a+b+c} ")
def promedioArreglo(lista:list):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=webo.mean(lista)
    print(f"el promedio es {p}")


if __name__ == '__main__':
    suma (10,52)
    suma (23,47,50)
    suma (12)

    lista2=[1,2,3,4,5]
    #lista2=lista
    promedioArreglo(lista2)
    #a esto se le llama referencia argumento
    print(lista2)


