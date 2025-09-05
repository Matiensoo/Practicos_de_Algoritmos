#Ejercicio 10

cinema = [True, True, True, False, False, True, True, True, False, False, False, False, False, False, True, True, True, True, True, False]

empty = 0

for seats in cinema:
    if not seats:
        empty +=1

print (f"La cantidad de butacas desocupadas es: {empty}")