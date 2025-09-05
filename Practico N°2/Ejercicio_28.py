#Ejercicio 28

import random

phrase = input ("ingrese sus 10 marcas favoritas: ")

list_phrase = phrase.split (" ")

print (random.choice(list_phrase))