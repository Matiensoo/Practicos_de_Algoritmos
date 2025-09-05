#Ejercicio 14

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

def function(number1, number2): 
    if number1 > number2:
        return number1
    else:
        return number2
    
function(number1, number2)

print (f"El mayor de los 2 numeros es {function(number1, number2)}")