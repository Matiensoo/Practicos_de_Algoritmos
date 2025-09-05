#Ejercicio 32

numbers = []

list = True

while list:
    enter = input("Ingrese un número (o 's' para salir): ")
    
    if enter == "s":
        list = False
         
    else:
        number = int(enter)  
        numbers.append(number)


print("Números ingresados:")
for num in numbers:
    print(num)


