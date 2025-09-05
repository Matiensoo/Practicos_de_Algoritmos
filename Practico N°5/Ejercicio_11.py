#Ejercicio 11

number = int(input("Ingrese un numero: "))

def function(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Impar"

function(number)

print (f"{function(number)}")