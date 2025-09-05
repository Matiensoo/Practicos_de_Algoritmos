#Ejercicio 16

binary_number = (input("ingrese un numero conformado solo por 0 y 1: "))

def binary(binary_number):
    if binary_number.count("1") == binary_number.count("0"):
        return True
    else:
        return False

binary(binary_number)

print (f"¿Tiene la misma cantidad de 1 que de 0?: {binary(binary_number)}")