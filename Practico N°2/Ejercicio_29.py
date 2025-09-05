#Ejercicio 29

amount = int(input("¿Cuántas notas desea ingresar? "))

qualifications = []
for _ in range(amount):
    qualification = float(input("Ingrese una nota: "))
    qualifications.append(qualification)

print (f"Se han ingresado las siguientes notas: {qualifications}")