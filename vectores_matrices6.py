import random
n = 3
m = 4
matriz = [[random.randint(0, 20) for _ in range(m)] for _ in range(n)]

print("Matriz:")
for fila in matriz:
    print(fila)

suma_total = 0
for fila in matriz:
    suma_total += sum(fila)

print(f"Suma de todos los elementos en la matriz: {suma_total}")
