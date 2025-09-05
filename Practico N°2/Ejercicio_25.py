#Ejercicio 25

numbers = [123, 4, 56, 7890, 12] 

amount = []

for number in numbers:
    digits = len(str(number))  
    amount.append(digits)

print(f"Lista de números: {numbers}")
print(f"Cantidad de dígitos de cada número: {amount}")