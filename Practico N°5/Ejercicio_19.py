#Ejercicio 19

def mayus_letter(text):
    result = ''
    new_word = True  

    for character in text:
        if new_word and 'a' <= character <= 'z':
            result += chr(ord(character) - 32)  
            new_word = False
        else:
            result += character
            if character == ' ':
                new_word = True
            else:
                new_word = False

    return result

print(mayus_letter("la letra inicial deberia estar en mayusculas"))

