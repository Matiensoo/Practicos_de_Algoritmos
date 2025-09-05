#Ejercicio 19

name = input("Danos un nombre: ")

list_name = ["juan", "paco", "pepe", "gustavo","felipe", "maximo", "santiago", "valentin"]

if name in list_name:
    print (f"Si, {name} esta dentro de la lista")
else:
    print ("El nombre no esta dentro de la lista")