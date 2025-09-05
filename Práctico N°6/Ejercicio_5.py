#Ejercicio 5

import os
import random

archive_name = "numeros_aleatorios.txt"


amount = int(input("¿Cuántos números desea generar? "))

with open(archive_name, "w") as archive:
    for i in range(amount):
        number = random.randint(1, 100)
        archive.write(f"{number}\n")

total_sum = 0
counter = 0

with open(archive_name, "r") as archive:
    for line in archive:
        number = int(line.strip())
        total_sum += number
        counter += 1

if counter > 0:
    average = total_sum / counter
    print(f"\nSuma total de los números: {total_sum}")
    print(f"Promedio de los números: {average}")
else:
    print("\nNo hay números en el archivo.")
