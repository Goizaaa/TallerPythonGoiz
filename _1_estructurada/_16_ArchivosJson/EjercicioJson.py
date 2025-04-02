import json
import sys
from operator import truediv


# esta es la version corta de abrir un archivo json
# abriendo el archivo JSON en modo lectura y with se encarga de cerrar

def vedad():

    try:
        informacion = open("tabla.json", "r", encoding="utf-8")
        tabla = json.load(informacion)

        for persona in tabla["personas"]:
            yield (persona['Id'],persona['Nombre'],persona['Edad'],persona['RFC'])


    except FileNotFoundError:
        print (RED,"error el archivo no existe ")
    except json.JSONDecodeError:
        print (RED,"error el archivo no existe ")
    except Exception as e:
        print (RED,"error el archivo no existe ")
    else:
        informacion.close()
        print(RESET,"archivo json cerrado")



if __name__ == '__main__':
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"
    i=1

    # se carga el contenifo del archivo JSON
    # la r significa que se va a leer de forma read

    for Id, Nombre, Edad, RFC in vedad():
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(YELLOW)
            case 4:
                sys.stdout.write(MAGENTA)
            case 4:
                sys.stdout.write(RESET)
        print(Id)
        print(Nombre)
        print(Edad)
        print(RFC)
          # libea para separar los datos

        if Edad >= 18:
             (print("es mayor de edad"))
        else:
             (print("es menor de edad"))

        print("------------------------------")# libea para separar los datos

        i+=1