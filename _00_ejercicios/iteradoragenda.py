
def extrae(agenda:tuple):
    i:int=0
    while(i<len(agenda)):
        nombre,correo,telefono=agenda[i]
        i+=1
        yield nombre,correo,telefono





if __name__ == '__main__':

    agenda=[]

    agenda.append(("Juan","juan@gmail.com","2224578989"))
    agenda.append(("Karla","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("Nick","Tlacuachitos32@gmail.com","248759854"))
    agenda.append(("Choco","Tlacuachitos@gmail.com","2487559823"))
    agenda.append(("Rolly","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("Kira","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("Antonio","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("irma","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("leticia","Tlacuachitos@gmail.com","2487598984"))
    agenda.append(("hola","Tlacuachitos9mail.com","24875956849"))

    for a,b,c in extrae(agenda):
       print(f"{a},{b},{c}")