#Ejercicio 18

width = int(input("Ingrese el ancho del cuadrado: "))

def print_sqare(width):
    for fila in range(width):
        if fila == 0 or fila == width - 1:
            print('#' * width)
        else:
            print('#' + ' ' * (width - 2) + '#')

print_sqare(width)