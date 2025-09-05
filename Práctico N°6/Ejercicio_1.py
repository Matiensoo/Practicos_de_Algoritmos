#Ejercicio 1

import os

archive_name = "palabras.txt"

amount = int(input("Cuántas palabras desea ingresar? "))


with open(archive_name, "w") as archive:
    for i in range(amount):
        word = input(f"Ingrese la palabra {i+1}: ")
        archive.write(word + "\n")


with open(archive_name, "r") as archive:
    lines = archive.readlines()

print("Palabras guardadas en el archivo:")
for line in lines:
    print(line.strip())

print(f"Total de líneas: {len(lines)}")

