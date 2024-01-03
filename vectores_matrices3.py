# Indique la cantidad de veces que se repite un determinado número en una matriz de nxm, así como las posiciones donde se repite. 
def buscar_numero(matriz, num_buscar):
    global reps
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num_buscar:
                print(f"Se encuentra el número en la matriz, en la posición [{i},{j}].")
                reps+=1
    if reps<=0:
        print("No se encuentra el número en la matriz.")
    else:
        print(f"se repite: {reps} veces")

reps=0
matriz = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [10, 11, 10, 12]]

num_buscar = 10
buscar_numero(matriz, num_buscar)