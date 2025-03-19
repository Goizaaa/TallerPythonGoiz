if __name__ == '__main__':

    mi_lista=[1,2,3]
    mi_lista.append(4)
    print(mi_lista)

    #añade los elementos a otra lista

    mi_lista=[1,2,3,4]
    otra_lista=[5,6,7]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #inserta un elemento en una posicion especial

    mi_lista=[1,2,3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #elimina el primer elemento de la lista

    mi_lista=[1,2,3,2]
    mi_lista.remove(2)
    print(mi_lista)

    #elimina y devuelve el elemento en una posicion especifica en una lista
    mi_lista=[1,2,3]
    elemento=mi_lista.pop(1)
    print(elemento)
    print(mi_lista)

    #devuelve el indice de la primera aparicion de un elemento

    mi_lista=[1,2,3,2]
    indice= mi_lista.index(2)
    print(indice)

    #devuelve el numero de veces que aparece un elemento

    mi_lista=[1,2,3,2]
    conteo =mi_lista.count(2)
    print(conteo)

    #ordena los elementos de una lista de forma acendente

    mi_lista=[3,1,4,2]
    mi_lista.sort()
    print(mi_lista)

    #en este de forma decendente


    mi_lista.sort(reverse=True)
    print (mi_lista)
    #invierte el orden
    mi_lista=[1,2,3,4]
    mi_lista.reverse()
    print(mi_lista)



    #en esta elimina todos los elementos de la lista
    mi_lista=[1,2,3]
    mi_lista.clear()
    print(mi_lista)

    #devuelve  una copia superficial de la lista
    mi_lista=[1,2,3]
    mi_lista2=mi_lista
    copia_lista=mi_lista.copy()
    mi_lista.append(4)
    print(copia_lista)
    print(mi_lista2)
#



