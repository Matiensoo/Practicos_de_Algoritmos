#Ejercicio 10

archive= input("ingrese el nombre de su archivo: ")

new_archive= ""

ext = len(archive)

for index in range(len(archive)):
    if archive[index] == " ":
        new_archive += "_"
    elif index < ext:
        new_archive +=archive[index]
    if archive[index] == ".":
        ext = index

new_archive = new_archive + "#" * (len(archive)-ext-1)

print(f"{new_archive}")