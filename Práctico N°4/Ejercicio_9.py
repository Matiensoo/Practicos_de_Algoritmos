#Ejercicio 9

#Ejercicio 7

import random

vector = []

result = []

for i in range(18):
    elements = random.randint(0,50)
    result.append(elements)

print (f"Elementos del vector: {result}")

vector_max = max(result)
vector_min = min(result)

vector.append(vector_max)
vector.append(vector_min)

print (f"El mayor y el menor de los elementos del vector: {vector}")