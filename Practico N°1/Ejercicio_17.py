#Ejercicio 17

number1= float(input("Ingrese un número: "))
number2= float(input("Ingrese otro número: "))
number3= float(input("Ingrese otro número: "))

if number1>number2 and number1>number3 and number2>number3:
    print({number3}, {number2}, {number1})

elif number1>number2 and number1>number3 and number3>number2:
    print({number2}, {number3}, {number1})

elif number2>number1 and number2>number3 and number1>number3:
    print({number3}, {number1}, {number2})

elif number2>number1 and number2>number3 and number3>number1:
    print({number1}, {number3}, {number2})

elif number3>number1 and number3>number2 and number1>number2:
    print({number2}, {number1}, {number3})

elif number3>number1 and number3>number2 and number2>number1:
    print({number1}, {number2}, {number3})
    

    
