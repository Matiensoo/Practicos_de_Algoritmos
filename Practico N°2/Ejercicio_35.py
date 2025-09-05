#Ejercicio 35

number = input("Ingrese un número de 6 cifras: ")

if len(number) == 6:
    invested = number[::-1]
    print(f"Numero ingresado: {number}. Invertido: {invested} ")
else:
    print("Debe ingresar un número de 6 cifras.")