#Ejercicio 12
import random

matrix = []

for row in range(4):
    rows=[]
    for columns in range(3):
        column = random.randint(0,99)
        rows.append(column)
    matrix.append(rows)

print(matrix)
