#Ejercicio 34

number = int(input("Ingrese un número: "))

max = number
min = number

for i in range(9):
    number = int(input("Ingrese otro número: "))
    
    if number > max:
        max = number
    
    if number < min:
        min = number

print(f"El número mayor es: {max}")
print(f"El número menor es: {min}")