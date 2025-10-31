#Ejercicio 1

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
       
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

list_1 = [76, 21, 34, 68, 31, 27, 53]

print (insertion_sort(list_1))