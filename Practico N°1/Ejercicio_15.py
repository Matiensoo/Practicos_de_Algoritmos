#Ejercicio 15
word1=(input("Ingrese un numero entero: "))
word2=(input("Ingrese un segundo numero entero: "))

if len(word1)>len(word2):
    print(f"La palabra con mas letras es {word1}")

elif len(word1)<len(word2): 
   print(f"La palabra con mas letras es {word2}")
    
else: print("Las palabras tienen la misma cantidad de letras")