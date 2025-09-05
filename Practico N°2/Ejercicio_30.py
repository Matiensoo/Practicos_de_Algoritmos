#Ejercicio 30

number = int(input("Ingrese un número positivo: "))

#Con for: 

for i in range(number, -1, -1):
    print(i)

#Con while 

while number >= 0:
    print(number)
    number -= 1