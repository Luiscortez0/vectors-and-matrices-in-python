# Desarrolla un algoritmo que determine si una matriz dada es una matriz identidad. 
# Una matriz identidad es una matriz cuadrada en la que todos los elementos de la diagonal principal son 1 y el resto son 0.
def matriz_identidad(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    if n_filas != n_columnas:
        return False

    for i in range(n_filas):
        for j in range(n_columnas):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False

    return True

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

for fila in matriz:
    print(fila)
print("¿Es una matriz identidad?", matriz_identidad(matriz))