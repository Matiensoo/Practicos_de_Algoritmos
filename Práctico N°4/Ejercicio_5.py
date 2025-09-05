#Ejercicio 5

vector = []

amount = int(input("ingrese elementos tendra el vector (preferentemente 20 elementos): "))


for elements in range(amount):
    elements = int(input("ingrese un numero deseado: "))
    vector.append(elements)

x = int(input(f"ingrese una posicion x (desde 0 - {amount}): "))
y = int(input(f"ingrese una posicion y (desde 0 - {amount}): "))

print(vector[x:y+1])


