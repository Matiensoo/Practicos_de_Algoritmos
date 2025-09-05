#Ejercicio 8

import random

vector = []

result = []

for i in range(18):
    elements = random.randint(0,50)
    result.append(elements)

print (f"Elementos del vector: {result}")

vector_result = sum(result) / 18

vector.append(vector_result)

print (f"El promedio de los elementos del vector: {vector_result}")