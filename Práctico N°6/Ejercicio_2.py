#Ejercicio 2

import random
import os

with open("numeros.txt", "w") as archive:
    for _ in range(10):
        number = random.randint(1, 100)
        archive.write(f"{number}\n")