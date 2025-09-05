#Ejercicio 4

names = []

amount = int(input("Cuantos nombres quiere ingresar? "))

for name in range(amount):
    name = input("ingrese los nombres deseados: ")
    names.append(name)

print (f"{names} zzz")