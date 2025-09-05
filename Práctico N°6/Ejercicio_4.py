#Ejercicio 4

import os

import random

archive_name = "numeros2.txt"

amount = int(input("¿Cuántos números desea generar? "))

numbers = []
for i in range(amount):
    number = random.randint(1, 10)
    numbers.append(number)

with open(archive_name, "w") as archive:
    for number in numbers:
        archive.write(f"{number}\n")

print(f"\nSe generó el archivo '{archive_name}' con los siguientes números:")
print(numbers)

with open(archive_name, "r") as archive:
    counter_five = 0
    for line in archive:
        if int(line.strip()) == 5:
            counter_five += 1

print(f"\nCantidad de números iguales a 5 en el archivo: {counter_five}")