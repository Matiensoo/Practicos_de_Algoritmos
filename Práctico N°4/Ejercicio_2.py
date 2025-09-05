#Ejercicio 2

numbers = []

for elements in range(5):
    elements = input("ingrese 5 numeros: ")
    numbers.append (elements)

new_numbers = []

for elements in reversed(numbers):
    new_numbers.append(elements)

print (new_numbers)
    


