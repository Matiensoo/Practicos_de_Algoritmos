#Ejercicio 8

ages = {"Juan": 30, "María": 25, "Pedro": 35}

ages ["Ana"] = 28

for k, v in ages.items():
    print (f"{k}, {v}")

name = input("Ingrese un nombre para comprobar que esta en el diccionario: ")

if name in ages:
    print ("El nombre esta dentro del diccionario")
else:
    print ("El nombre no esta dentro del diccionario")
