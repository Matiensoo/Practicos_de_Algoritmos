#Ejercicio 13

import random

matrix_list = []

for row in range(5):
    rows=[]
    for xx in range(4):
        x = random.randint(0,99)
        rows.append(x)
    matrix_list.append(rows)

matrix_column = []

for column in range(4):
    columns = []
    for yy in range(5):
        columns.append(matrix_list[yy][column])
    matrix_column.append(columns)
        

print(matrix_list)
print(matrix_column)
