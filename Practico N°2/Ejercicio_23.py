#Ejercicio 23

qualification1 = int(input("ingrese la primera nota: "))

qualification2 = int(input("ingrese la segunda nota: "))

qualification3 = int(input("ingrese la tercera nota: "))

qualification4 = int(input("ingrese la cuarta nota: "))

qualification5 = int(input("ingrese la quinta nota: "))

qualification6 = int(input("ingrese la sexta nota: "))

qualification7 = int(input("ingrese la septima nota: "))

qualification8 = int(input("ingrese la octava nota: "))

list_qualifications = [qualification1, qualification2, qualification3, qualification4, qualification5, qualification6, qualification7, qualification8]

result = sum(list_qualifications) / len(list_qualifications)

print (f"el promedio es de: {result:.2f}")