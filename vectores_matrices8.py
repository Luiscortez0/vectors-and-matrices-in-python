# Se te proporcionan dos matrices cuadradas, A y B, de tamaño NxN. 
# Su tarea es desarrollar un algoritmo que realice la suma de estas dos matrices, resultando en una tercera matriz cuadrada, C.
def sumar_matrices(matriz1,matriz2):
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            matriz_resultado[i][j]=matriz1[i][j]+matriz2[i][j]
    
    for fila in matriz_resultado:
        print(fila)

matriz1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matriz2 = [[10, 11, 12],[13, 14, 15],[16, 17, 18]]
matriz_resultado = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

print("matriz 1")
for fila in matriz1:
    print(fila)
print(" ")
print("matriz 2")
for fila in matriz2:
    print(fila)
print(" ")
print("suma de matrices: ")
sumar_matrices(matriz1,matriz2)