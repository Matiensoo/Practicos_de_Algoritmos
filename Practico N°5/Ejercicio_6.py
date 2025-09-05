#Ejercicio 6

number = int(input("ingrese un numero: "))

def function(number):
    for i in range(11):
        print (f"{number} x {i} = {number * i}")

function(number)