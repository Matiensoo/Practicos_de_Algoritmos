#Ejercicio 6

import random

vector = []

for i in range(30):
    throw = random.randint(1,100)
    vector.append(throw)
print(vector)


x = int(input(f"ingrese una posicion x (desde 0 - 29): "))
y = int(input(f"ingrese una posicion y (desde 0 - 29): "))

vector[x], vector[y] = vector[y], vector[x]

print (f"Con las posiciones {x} y {y}, convertido {vector}")