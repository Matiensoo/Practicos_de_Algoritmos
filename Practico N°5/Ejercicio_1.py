#Ejercicio 1

frame = int(input("Ingrese un valor: "))

def square (frame):
    print(f"El numero ingresado al cuadrado es {frame * frame}")

square(frame)
    
#Inciso a

frame = int(input("Ingrese un valor: "))

def square (frame):
    print(f"El numero ingresado al cuadrado es {frame * frame}")
    print(f"las variables locales son: {locals()}")

square(frame)

#Inciso b

frame = int(input("Ingrese un valor: "))

def square(frame):
    frame1 = 2
    frame2 = 3
    frame3 = 7
    print(f"El numero ingresado al cuadrado es {frame * frame}")
    print(f"las variables locales son: {locals()}")

square(frame)

    