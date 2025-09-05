#Ejercicio 33

amount = int(input("¿Cuántos números desea ingresar? "))

pair_result = 0
odd = False


for i in range(amount):
    number = int(input("Ingrese un número: "))
    if number == 99:
        print("Se interrumpió la carga por ingresar 99.")
        break
    elif number % 2 == 0:
        pair_result += number
    elif number % 1 == 0 :
        break

print(f"Suma de números pares: {pair_result}")
if odd:
    print("Se ingresaron impares.")