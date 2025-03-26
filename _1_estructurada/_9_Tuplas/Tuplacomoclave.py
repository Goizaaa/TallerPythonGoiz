if __name__ == '__main__':

    diccionario={
        ("id", "int"):'2',
        'nombre':'juan',
        'apellido':'gutierrez'
    }


    diccionario[("Ana",25)]="estudiante"
    diccionario[("Luis",30)]="ingeniero"
    diccionario[("Carlos",40)]="abogado"

    ocupacion_ana=diccionario[("Ana",25)]
    ocupacion_luis=diccionario[("Luis",30)]
    ocupacion_carlos=diccionario[("Carlos",40)]


    print(f"Ana es:{ocupacion_ana}")
    print(f"Luis es:{ocupacion_luis}")
    print(f"Carlos es:{ocupacion_carlos}")