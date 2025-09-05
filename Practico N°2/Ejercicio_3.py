#Ejercicio 3
message= str(input("Ingrese una frase: "))

if len(message)>5:
    print(message[0],message[1],message[2])
else:
    print("La frase debe tener mas de 5 caracteres")
