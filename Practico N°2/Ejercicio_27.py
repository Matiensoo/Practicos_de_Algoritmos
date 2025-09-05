#Ejercicio 27

import random

throws = [ ]

for i in range(25000):
    throw = random.randint(1,6)

    throws.append(throw)

result = sum(throws) / len(throws)

print (result)    

#No se nota una diferencia muy notable, solo que aumenta el numero de decimales en el promedio de la tirada