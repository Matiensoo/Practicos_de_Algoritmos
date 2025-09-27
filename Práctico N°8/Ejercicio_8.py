class Pila:
    def __init__ (self):
        self.list = []
        
    def push (self, elements):
        self.list.insert(0,elements)

    def delete (self):
        if self.empty_list():
            return None
    
    def pop(self):
        self.list.pop(0)
    
    def empty_list(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def show (self):
        print (self.list)

inverted_word = Pila()

add = ""

word = input("Ingrese su cadena de texto: ")

for char in word:
    if char != " ":
        add += char
    else:
        inverted_word.push(add)
        add = ""
        inverted_word.push(" ")
inverted_word.push(add)

print(word)

inverted_word.show()