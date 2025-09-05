#Ejercicio 17

movie1 = input("Diga el nombre de la primera pelicula: ")

movie2 = input("Diga el nombre de la segunda pelicula: ")

movie3 = input("Diga el nombre de la tercera pelicula: ")

movie4 = input("Diga el nombre de la cuarta pelicula: ")

movie5 = input("Diga el nombre de la quinta pelicula: ")

movie6 = input("Diga el nombre de la sexta pelicula: ")

movie7 = input("Diga el nombre de la septima pelicula: ")

movie8 = input("Diga el nombre de la octava pelicula: ")

movie9 = input("Diga el nombre de la novena pelicula: ")

movie10 = input("Diga el nombre de la décima pelicula: ")

movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10]

number = int(input("ingrese un numero del uno al diez: "))

if number == 1:
    print(movies[0])
elif number == 2:
    print(movies[1])
elif number == 3:
    print(movies[2])
elif number == 4:
    print (movies[3])
elif number == 5: 
    print (movies[4])
elif number == 6: 
    print (movies[5])
elif number == 7: 
    print (movies[6])
elif number == 8: 
    print (movies[7])
elif number == 9: 
    print (movies[8])
elif number == 10: 
    print (movies[9])
else:
    print ("Número fuera de rango")
