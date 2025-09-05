#Ejercicio 3

import os

with open("colores.txt", "w") as archive:
    for i in range(5):
        color = input(f"Ingrese el color {i+1}: ")
        archive.write(f"{color}\n")