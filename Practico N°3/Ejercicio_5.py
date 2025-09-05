#Ejercicio 5

qualifications = {}


amount = int(input("¿Cuántos estudiantes quieres ingresar? "))


for i in range(amount):
    name = input(f"Ingrese el nombre del estudiante #{i + 1}: ")
    score = float(input(f"Ingrese la puntuación de {name}: "))
    qualifications[name] = score


student = input("Ingresa el nombre del estudiante para consultar su puntuación: ")

if student in qualifications:
    print(f"{student} obtuvo una puntuación de {qualifications[student]}")
else:
    print(f"No se encontró al estudiante '{student}'.")