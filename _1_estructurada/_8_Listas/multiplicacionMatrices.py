if __name__ == '__main__':

    matrizA=[[1,2,3],[4,5,6]]
    matrizB=[[-1,0],[0,1],[1,1]]

    res=[[0,0],[0,0]]

    tamA=len(matrizA)
    tamB=len(matrizB)

    print(f"el tamaño de la matriz A es{tamA}")
    print(f"el tamaño de la matriz B es{tamB}")

    for i in range(len(matrizA)):
        for e in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                res[i][e]+=matrizA[i][k]*matrizB[k][e]

    print(f"el resultado es{res}")
