if __name__ == '__main__':
    x=int (input("ingresa un numero: "))
    y=int (input("ingresa la potencia: "))

    i:int=0;
    pot:int=1;

    while i<y:
        pot=pot*x
        i=i+1
        #tambien podemos escribir pot=pot-x; i+=1
        print(f"el resultado de {x} a la potencia de {y} es: {pot}")

