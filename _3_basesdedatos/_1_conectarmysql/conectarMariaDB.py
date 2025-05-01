import mariadb

def conectar_y_consultar():
    try:
        conexion =mariadb.connect(

            host="localhost",
            database="almacenas",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))
        print("conexion a la base de datos del servidor Ounus")

        cursor =conexion.cursor()
        consulta ="select * from usuarios"
        cursor.execute((consulta))


        resultados =cursor.fetchall()
        print("resultado ", type(resultados))
        print("datos en la tabla:")
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre de usuario: {fila[1]}, Correo: {fila[2]}, contraseña: {fila[3]}, Id_rol: {fila[4]}")

        consultae = "select * from roles"
        cursor.execute((consultae))

        resultados = cursor.fetchall()
        print("resultado ", type(resultados))
        print("datos en la tabla:")
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre de usuario: {fila[1]}, Correo: {fila[2]}, contraseña: {fila[3]}, Id_rol: {fila[4]}")


    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("conexion cerrada")


if __name__ == '__main__':
    conectar_y_consultar()