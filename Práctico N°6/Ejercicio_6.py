#Ejercicio 6 

import os
import random

def create_archive(archive_name):
    with open(archive_name, "w") as archive:
        for i in range(250):
            number = random.randint(1, 100)
            archive.write(f"{number}\n")

create_archive("archivo250.txt")