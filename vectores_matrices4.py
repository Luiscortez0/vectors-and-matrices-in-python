# Dado un array de números enteros, encuentre el valor máximo y mínimo en el array.
array = [2, 3, 1, 7, 10]
maximo = array[0]
minimo = array[0]

for i in range(len(array)):
    if array[i] > maximo:
        maximo=array[i]
    if array[i] < minimo:
        minimo=array[i] 
        
print(f"El valor maximo es: {maximo}")
print(f"El valor minimo es: {minimo}")