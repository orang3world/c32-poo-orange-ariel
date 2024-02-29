# Crear un algoritmo para calcular la sumatoria de los primeros cien
# números (del 01 al 100) con un ciclo while.
""" iterar del 1 al 100 sumando al anterior 
    contador += 1 , while contador <= 100
    segunda variable ejemplo suma += contador"""

contador = 1
suma = 0
while contador <=100:
    suma += contador
    contador +=1
print(f'La suma final , es igual a : {suma}')
