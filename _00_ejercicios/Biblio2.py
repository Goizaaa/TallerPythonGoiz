
class Biblioteca:
    def __init__ (self):
        self.__Titulo:str=""
        self.__ISBN:int=1258
        self.__Autor:str=""

    def getTitulo(self)->str:
        return self.__Titulo

    def getISBN(self)->int:
        return self.__ISBN

#el @property se pone arriba de los def
    #@property  #este significa que se convertira en una propiedad de lectura
    def getAutor(self)->str:
        return self.Autor


    def setTitulo(self,nombre:str):
        self.Autor=nombre


    def setISBN(self,isbn:int):
        self.ISBN=isbn



    def setAutor(self,Autor:str):
        self.Autor=Autor

if __name__ == '__main__':
    Biblioteca=Biblioteca()
    Biblioteca.setTitulo("Don quijote de la mancha")

    print(Biblioteca.getTitulo)
