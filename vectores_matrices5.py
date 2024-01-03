# Implementa un algoritmo que invierta los elementos de un array de tamaño n dado.
def invertir_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

array = [2, 3, 1, 7, 10]
print("Array original:", array)
invertir_array(array)
print("Array invertido:", array)
