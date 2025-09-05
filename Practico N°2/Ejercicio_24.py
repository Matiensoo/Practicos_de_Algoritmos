#Ejercicio 24

#Con listas:

phrase = input ("ingrese una frase: ")

list_phrase = phrase.split (" ")

print (len(list_phrase))

#Sin listas:

counter = 1

for word in phrase:
    if word == " ":
        counter +=1

print (counter)



