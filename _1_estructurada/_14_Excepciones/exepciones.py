if __name__ == '__main__':
    try:
        #este es el codigo que puede causar la excepcion
        numero=int(input("introduce un numero: "))
        resultado=10/numero

    except ValueError:
        #este manejo de la excepcion si se introduce un valor no valido
        print("ERRORRRRRRRRRRRRRRRRRR, chamo tienen que ser numeros enteros.")
    except ZeroDivisionError:
        #manejo de la excepcion si se intenta dividir por cero
        print("ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR, pe no se puede dividir entre cero.")
    else:
        #este se ejecuta si no hubo excepciones
        print("el sesultado es: ", resultado)
    finally:
        print("fin del programa")

