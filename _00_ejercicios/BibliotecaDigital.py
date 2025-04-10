#Desarrolla un programa en python que utilice
#la POO para registrar un libro (ISBN,TITULO Y AUTOR)
#LOS ATRIBUTOS DEBE ESTAR EN PRIVADO
#DEBES TENER UN CONSTRUCTOR PARA EL REGISTRO
#DEBES TENER SOLO GETTERS DE CADA ATRIBUTO

#EN OTRA CLASE DEBERA REGISTRAR UNA COLECCION DE LIBROS
#EN ESTA CLASE DEBES TENER ADD, DELETE Y SHOW


class Biblioteca:
    def __init__(self, Titulo: str, Autor: str, ISBN: int):
        self.Titulo= Titulo
        self.Autor = Autor
        self.ISBN = ISBN



class Libros:

    def __init__(self):
        self.lista=[]

    def addLibro(self,Titulo, Autor, ISBN):
        self.lista.append(Biblioteca(Titulo,Autor, ISBN))

    def show(self):
        for obj in self.lista:
            print(f"Titulo: {obj.Titulo}")
            print(f"Autor: {obj.Autor}")
            print(f"ISBN: {obj.ISBN}")
            print("--------------------------------")

if __name__ == '__main__':

    escolar=Libros()
    escolar.addLibro("Don quijote de la mancha", "Miguel de Cervantes","84-7758-024-3")
    escolar.show()