if __name__ == '__main__':
    x = int(input("ingresa el primer numero a multiplicar: "))
    y = int(input("ingresa el segundo numero a multimplicar: "))

    i: int = 0;
    mul: int = 0;


    while i < y:
        mul = mul+x
        i = i + 1
#el print dentro del while muestra todas las vuelas que hace para llegar al resultado
    print(f"el resultado de la multiplicacion es: {mul}")
