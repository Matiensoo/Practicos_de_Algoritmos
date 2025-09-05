#Ejercicio 7

x = int(input("Ingrese un punto en x: "))
y = int(input("Ingrese un punto en y: "))

def cuadrante(x,y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0 :
        return 2
    elif x < 0 and y < 0 :
        return 3
    elif x > 0 and y < 0 :
        return 4

cuadrante(x,y)

if x == 0 and y == 0:
    print ("Las coordenadas estan en el origen")
else:
    print (f"Las coordenadas ({x},{y}) esta en el cuadrante {cuadrante(x,y)}")