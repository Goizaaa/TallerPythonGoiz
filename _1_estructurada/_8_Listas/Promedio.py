import statistics as was

if __name__ == '__main__':

    numeros=[10,20,50,80,90,30,40]
    conteo=0;
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor
        conteo +=1

    promedio=suma/conteo
    print(promedio)


    #opcion 2 es mas lenta

    suma=0
    for v in numeros:
        suma +=valor
    promendo=suma/len(numeros)
    print(promedio)

    #opcion rapida en este le ponemos un alias a la libreria, eso significa que solo sera utilizado en donde sea invocado
    #mean es la funcion para invocarlo, es la funcion para calcular el promedio de una lista

    promedio== was.mean (numeros)
    print(promedio)

