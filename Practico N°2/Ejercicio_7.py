#Ejercicio 7

phrase= str(input("Ingrese una frase: "))

for i in range(len(phrase)):
    if i % 2==0:
        print(phrase[i])