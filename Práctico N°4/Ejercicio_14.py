#Ejercicio 14

import random

matrix_list = []

for row in range(4):
    rows=[]
    for xx in range(3):
        x = random.randint(0,99)
        rows.append(x)
    matrix_list.append(rows)
sum_matrix_list0 = sum(matrix_list[0])
sum_matrix_list1 = sum(matrix_list[1])
sum_matrix_list2 = sum(matrix_list[2])
sum_matrix_list3 = sum(matrix_list[3])
sum_matrix_list = sum_matrix_list0 + sum_matrix_list1 + sum_matrix_list2 + sum_matrix_list3

matrix_column = []

for column in range(3):
    columns = []
    for yy in range(4):
        columns.append(matrix_list[yy][column])
    matrix_column.append(columns)
sum_matrix_column0 = sum(matrix_column[0])
sum_matrix_column1 = sum(matrix_column[1])
sum_matrix_column2 = sum(matrix_column[2])    
sum_matrix_column = sum_matrix_column0 + sum_matrix_column1 + sum_matrix_column2  

print(matrix_list)
print(matrix_column)

print(sum_matrix_list)
print(sum_matrix_column)




