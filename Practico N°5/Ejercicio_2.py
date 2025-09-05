#Ejercicio 2 

#Inciso a

n = 5
frame = int(input("Ingrese un valor: "))

def square(frame):
    print(f"El numero ingresado al cuadrado es {frame * frame}")
    print(f"Valor de n al cuadrado: {n * n}")

square(frame)

#Inciso b

n = 5
frame = int(input("Ingrese un valor: "))

def square (frame):
    n = 7
    print(f"El numero ingresado al cuadrado es {frame * frame}")
    print(f"Valor de n al cuadrado: {n * n}")

square(frame)

#Lo que sucede, es que se crea otra variable local "n" con distinto numero, pero no se modifica la n global

#Inciso c

#Para cambiar el valor de n de forma global, escribiremos global n dentro de la funcion.

n = 5
frame = int(input("Ingrese un valor: "))

def square(frame):
    global n 
    n = 7
    print(f"El numero ingresado al cuadrado es {frame * frame}")
    print(f"Valor de n al cuadrado: {n * n}")

square(frame)
print(f"Ahora se ha modificado el valor de n en forma global, ya que n ahora es {n}")
