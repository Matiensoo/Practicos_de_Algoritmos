#Ejercicio 26

import random

throws = [ ]

for i in range(20):
    throw = random.randint(1,6)

    throws.append(throw)

result = sum(throws) / len(throws)

print (result)    





   


