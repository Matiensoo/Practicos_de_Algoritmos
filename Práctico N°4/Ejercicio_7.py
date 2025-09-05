#Ejercicio 7

import random

vector = []

result = []

for i in range(18):
    elements = random.randint(0,50)
    result.append(elements)

print (f"Elementos del vector: {result}")

vector_result = sum(result)

vector.append(vector_result)

print (f"Suma de elementos del vector: {vector_result}")



