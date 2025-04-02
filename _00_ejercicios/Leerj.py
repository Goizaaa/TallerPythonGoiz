import json
from operator import truediv


# esta es la version corta de abrir un archivo json
# abriendo el archivo JSON en modo lectura y with se encarga de cerrar

def vedad():
    with open("tabla.json", "r", encoding="utf-8") as archivo:
        tabla = json.load(archivo)

    for persona in tabla["personas"]:
        yield (persona['Id'],persona['Nombre'],persona['Edad'],persona['RFC'])






if __name__ == '__main__':

    # se carga el contenifo del archivo JSON
    # la r significa que se va a leer de forma read

    for Id, Nombre, Edad, RFC in vedad():
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

