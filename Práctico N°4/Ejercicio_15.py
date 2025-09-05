#Ejercicio 15

import random

a = []

for row in range(4):
    rows=[]
    for xx in range(3):
        x = random.randint(0,99)
        rows.append(x)
    a.append(rows)

b = []

sum_matrix_list0 = sum(a[0])
sum_matrix_list1 = sum(a[1])
sum_matrix_list2 = sum(a[2])
sum_matrix_list3 = sum(a[3])

b.append(sum_matrix_list0)
b.append(sum_matrix_list1)
b.append(sum_matrix_list2)
b.append(sum_matrix_list3)

matrix_columns = []

for column in range(3):
    columns = []
    for yy in range(4):
        columns.append(a[yy][column])
    matrix_columns.append(columns)

c = []

sum_matrix_list0 = sum(matrix_columns[0])
sum_matrix_list1 = sum(matrix_columns[1])
sum_matrix_list2 = sum(matrix_columns[2])
  

c.append(sum_matrix_list0)
c.append(sum_matrix_list1)
c.append(sum_matrix_list2)

print(a)
print(b)
print(c)
