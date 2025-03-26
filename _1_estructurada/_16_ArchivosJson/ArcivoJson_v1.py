import json

if __name__ == '__main__':
    # esta es la version corta de abrir un archivo json
    #abriendo el archivo JSON en modo lectura y with se encarga de cerrar

    with open("datos.json","r", encoding="utf-8") as archivo:
        datos= json.load(archivo)
        #se carga el contenifo del archivo JSON
        #la r significa que se va a leer de forma read


        for persona in datos["personas"]:
            print("Nombre: ", persona["nombre"])
            print("Edad: ", persona["edad"])
            print("Ciudad: ", persona["ciudad"])
            print("Estado: ", persona["estado"])
            print("------------------------------")#libea para separar los datos
