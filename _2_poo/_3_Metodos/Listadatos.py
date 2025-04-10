class ListaDatos:
    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura


if __name__ == '__main__':
    lista=[]
    lista.append(ListaDatos("1258658","Juan Calderon","Español"))
    lista.append(ListaDatos("1234765","Cecilia Rocha","Metodos"))
    lista.append(ListaDatos("5432123","Federico Cruz","Ciencias"))
    lista.append(ListaDatos("1250987","Paola Flores","Fisica"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura}")
        print("--------------------------------")