#Ejercicio 12

character = input("Ingrese un caracter: ")
width = int(input("Ingrese el ancho inicial del triangulo: "))

def triangle(character, width):
    for i in range(width, 0, -1):
        print(character * i)

triangle(character,width)
