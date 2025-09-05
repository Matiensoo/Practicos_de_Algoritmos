#Ejercicio 3

import random

vector = []

for i in range(20):
    throw = random.randint(5,20)

    vector.append(throw)


number = int(input("Ingrese un numero: "))

if number in vector:
    print ("El numero ingresado esta dentro del vector")
else:
    print ("El numero no esta dentro del vector")