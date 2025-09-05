#Ejercicio 20

def compare_arrays(arr1, arr2, search_commons):
    result = []

    if search_commons:
     
        for elem1 in arr1:
            finish = False
            for r in result:
                if r == elem1:
                    finish = True
                    break
            if not finish:
                for elem2 in arr2:
                    if elem1 == elem2:
                        result.append(elem1)
                        break
    else:
        
        for elem1 in arr1:
            found = False
            for elem2 in arr2:
                if elem1 == elem2:
                    found = True
                    break
            if not found:
                finish = False
                for r in result:
                    if r == elem1:
                        finish = True
                        break
                if not finish:
                    result.append(elem1)

        for elem2 in arr2:
            found = False
            for elem1 in arr1:
                if elem2 == elem1:
                    found = True
                    break
            if not found:
                finish = False
                for r in result:
                    if r == elem2:
                        finish = True
                        break
                if not finish:
                    result.append(elem2)

    return result


print(compare_arrays([1, 2, 3], [3, 4, 5], True))   
print(compare_arrays([1, 2, 3], [3, 4, 5], False))  
