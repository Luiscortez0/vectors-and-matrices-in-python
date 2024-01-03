#Modifica el programa para que en vez de decirte si el número está o no dentro del array, te diga cuantas veces se repite el número y en que posiciones lo hace.
array = [1, 3, 5, 7, 5]
numero_a_buscar = 5
repes=0

resultado = "No se encuentra el número en el array."

for i in range(len(array)):
    if array[i] == numero_a_buscar:
        resultado = f"Sí se encuentra el número en el array, posicion:{i+1}"
        print(resultado)
        repes+=1

print(f"repeticiones: {repes}")