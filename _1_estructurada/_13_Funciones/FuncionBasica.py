def suma(a:int,b:int)->int:
    return a+b
def arreglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':
    print(f"la suma es de {suma(15,22)}")
    lista=[1,2,3,4,5,6]
    print(f"la suma del arreglo es {arreglo(lista)}")