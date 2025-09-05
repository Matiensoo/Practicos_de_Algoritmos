#Ejercicio 16

import random

matrix = []


for row in range(5):
    rows=[]
    for columns in range(6):
        column = random.randint(1,6)
        rows.append(column)
    matrix.append(rows)

matrix [4] = [0 for i in range(6)]

print(matrix)