
if __name__ == '__main__':

    n:int= int(input("Ingresa un numero de nombres a guardar"))
    indi=[0,0,0,0,0,0,0,0,0,0]
    extra:int=1
    for i in range(n):
        nombre:str= str(input("Ingresa el nombres a guardar: "))
        tam=len(nombre)
        match tam:
            case 1: indi[0]+=1
            case 2: indi[1]+=1
            case 3: indi[2]+=1
            case 4: indi[3]+=1
            case 5: indi[4]+=1
            case 6: indi[5]+=1
            case 7: indi[6]+=1
            case 8: indi[7]+=1
            case 9: indi[8]+=1
            case 10: indi[9]+=1
            case _: extra+=1

    i:int=1
    for elemento in indi:
        print(f"el total de nombres con {i} letras: {elemento}")
        i+=1
    print(f"el total de nombres con mas de 10 letras: {extra}")





