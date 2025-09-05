#Ejercicio 31

positives = 0
negatives = 0

for i in range(10):
    number = int(input("Ingrese 10 números: "))
    if number >= 0:
        positives += 1
    else:
        negatives -= 1

print(f"Números positivos: {positives}")
print(f"Números negativos: {negatives}")