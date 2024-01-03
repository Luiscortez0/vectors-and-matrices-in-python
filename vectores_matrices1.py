#Haz las modificaciones para verificar las veces que se repite un número en el array. 
array = [1, 3, 5, 7, 5]
numero_a_buscar = 5
repes=0

resultado = "No se encuentra el número en el array."

for i in range(len(array)):
    if array[i] == numero_a_buscar:
        resultado = "Sí se encuentra el número en el array."
        repes+=1
        
print(resultado)
print(F"repeticiones: {repes}")