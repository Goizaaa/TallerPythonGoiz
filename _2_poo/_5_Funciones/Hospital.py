
#poner __ es como poner en privado los atributos

class Hospital:
    def __init__ (self):
        self.__NombrePaciente:str=""
        self.__nss:int=1258
        self.__enfermedad:str=""

    def getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__nss

#el @property se pone arriba de los def
    #@property  #este significa que se convertira en una propiedad de lectura
    def getEnfermedad(self)->str:
        return self.enfermedad


    def setNombrePaciente(self,nombre:str):
        self.NombrePaciente=nombre


    def setNss(self,nss:int):
        self.nss=nss



    def setEnfermedad(self,enfermedad:str):
        self.enfermedad=enfermedad

if __name__ == '__main__':
    hospital=Hospital()
    hospital.setNombrePaciente("Juan")

    print(hospital.getNombrePaciente)
