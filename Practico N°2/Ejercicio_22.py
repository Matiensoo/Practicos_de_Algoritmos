#Ejercicio 22

names = [ ]

surnames = [ ]

amount = int(input("ingrese la cantidad de nombres deseados: "))

for _ in range(amount):
    full_names = input("ingrese un nombre y apellido: ")
    parts = full_names.split(" ")

    if len(parts) == 2:
        names.append (parts[0])
        surnames.append (parts[1])

        print (names)

        print (surnames)

    else: 
        print ("ingrese solo nombre y apellido")
        



