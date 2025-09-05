#Ejercicio 12

phrase = input("Ingrese una frase: ")

word= " "

for char in phrase:
    if char != " ": 
        word +=char
    else:
        print(word)
        word= " "
        
if word:
    print(word)