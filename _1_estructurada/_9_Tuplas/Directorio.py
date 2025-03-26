if __name__ == '__main__':

    agenda={}

    agenda["GOAT800717"]=("Tomas Gonzales","csctomasgonzales@gmail.com","2223456765")
    agenda["GOAT800432"]=("Luis Gonzalez","luis85@gmail.com","2223456345")
    agenda["WASAT803456"]=("Tomas Gonzales","csctomasgonzales@gmail.com","2223456765")
    agenda["GOAT800222"]=("Tomas Gonzales","csctomasgonzales@gmail.com","2223456765")
    agenda["GOAT345564"]=("Tomas Gonzales","csctomasgonzales@gmail.com","2223456765")

    nombre,correo,numero=agenda["GOAT800717"]

    print(f"los datos del rfc son{nombre}, {correo}, {numero}")