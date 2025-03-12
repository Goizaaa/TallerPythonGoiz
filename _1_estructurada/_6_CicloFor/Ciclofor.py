import sys

if __name__ == '__main__':
    print("---rango de 0 a 9---")
    for i in range(10):
        print (f"{i}")


    print("---rango de 6 a 11---")
    for i in range(6,12):
        print (f"{i}")


    print("---rango de 6 a 11 pero con incrementos---")
    for i in range(6, 12,3):
        print(f"{i}")


    print("---rango de 1 a 20 pero sin salto de linea---")
    for j in range(1,20):
        print (f"{j}", end=" ")


sys.stdout.write("Texto linea")
