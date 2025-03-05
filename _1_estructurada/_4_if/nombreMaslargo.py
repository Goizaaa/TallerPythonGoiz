if __name__ == '__main__':
    nombre=str(input("escribe un nombre: "))
    nombre2=str(input("escribe otro nombre: "))


    nombre3 = len(nombre)
    nombre4 = len(nombre2)

    if nombre3>nombre4:
        print (f"el mayor es : {nombre}")
    else:
        if nombre3<nombre4:
            print (f"el mayor es : {nombre2}")
        else:
            print (f"{nombre2} es igual de largo que : {nombre}")




