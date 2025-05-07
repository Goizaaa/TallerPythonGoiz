if __name__ == '__main__':
    palabra:str ="%s "
    lista:list =["nombre","apellido","nombre_usuario","edad","correo_electronico","contraseña"]

    #print(palabra)
    #palabra=palabra* len(lista)
    print(palabra)


    t=len(lista) #obtiene el numero total de una lista
    print(t)


    palabra=palabra *len(lista)
    print(palabra)

    campos=", ".join(lista)
    print(campos)




    querySQL=f"INSERT INTO tabla ({campos} ) VALUES ({palabra})"
    print(querySQL)

