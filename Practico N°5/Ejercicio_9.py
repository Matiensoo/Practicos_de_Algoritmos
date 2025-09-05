#Ejercicio 9

word = input("Ingrese una palabra: ")
letter = input("¿Que letra desea ingresar? ")

def function(letter):
    return word.count(letter)

function(letter)

if letter in word:
    print (f"La letra {letter} se repite {function(letter)} veces en la palabra {word}")
else:
    print(f"{letter} no esta dentro de {word}")
