#Ejercicio 15

numbers = []
amount = int(input("¿Cuantos numeros desea ingresar? "))

for i in range (amount):
    number = int(input(f"Ingrese {amount} numeros: "))
    numbers.append(number)

def average(numbers, amount):
    return sum(numbers) / amount

average(numbers, amount)

print (f"El promedio de los numeros ingresados es {average(numbers, amount)}")  