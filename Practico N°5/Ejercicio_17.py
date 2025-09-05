#Ejercicio 17

phrase = input("Ingrese una frase: ")
character = input("¿Qué letra desea ingresar? ")
phrase = phrase.lower()


def function(phrase,character):
    counter = 0
    for i in phrase:
        if i == character:
            counter = counter+1
            return counter
        else:
            counter = counter+1
    
function(phrase, character)

print (f"la letra {character} se encuentra en la posicion {function(phrase,character)}")

        
    
