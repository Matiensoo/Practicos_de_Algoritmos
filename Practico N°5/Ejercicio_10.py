#Ejercicio 10

words = []

for i in range (10):
    word = input("Ingrese 10 palabras: ")
    words.append(word)

letter = input("¿Que letra desea ingresar? ")

def function(letter):
    total = 0
    for word in words:
        total += word.count(letter)
    return total



amount_letters= function(letter)

if amount_letters > 0: 
    print (f"La letra {letter} se repite {amount_letters} veces en las palabras {words}")
else:
    print(f"{letter} no esta dentro de {words}")

