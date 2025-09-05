#Ejercicio 36

import random

a = int(input("Ingrese el primer número positivo: "))
b = int(input("Ingrese el segundo número positivo: "))


while a >= b:
    print("El primer numero debe ser menor que el segundo.")
    a = int(input("Ingrese el primer número positivo: "))
    b = int(input("Ingrese el segundo número positivo: "))


print(f"Números del intervalo [{a}, {b}]:")
for number in range(a, b + 1):
    print(number)


secret = random.randint(a, b)


lives = 10


while lives > 0:
    puzzle = int(input(f"Tienes {lives} vidas. Debes adivinar el número: "))
    
    if puzzle == secret:
        print("¡Felicidades! Adivinaste el número ")
        break
    else:
        lives -= 1
        if lives > 0:
            print("Incorrecto. Intenta otra vez.")
        else:
            print("¡Pucha! se te acabaron las vidas. ")
            print(f"El número correcto era: {secret}")
    



