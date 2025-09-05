#Ejercicio 13

number = int(input("Ingrese un numero entero: "))

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if prime_number(number):
    print(f"El número {number} es primo.")
else:
    print(f"El número {number} no es primo.")

