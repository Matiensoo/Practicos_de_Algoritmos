class Pila:
    def __init__ (self):
        self.list = []
        
    def push (self, elements):
        self.list.append(elements)

    def delete (self):
        if self.empty_list():
            return None
        
        return self.list.pop()
    
    def add_back (self, elements):    

        self.list.insert(0,elements)
        return self.list
    
    def empty_list(self):
        return len(self.list) == 0
    
    def show (self):
        print (self.list)

W = Pila()
W_Inverted = Pila()

Word = input("Ingrese una palabra cualquiera: ")

for letter in Word:
    W.push(letter)


for letter in reversed(Word):
    W_Inverted.push(letter)

print("Pila normal:")
W.show()
print("Pila invertida:")
W_Inverted.show()

palindromo = True
while not W.empty_list() and not W_Inverted.empty_list():
    if W.delete() != W_Inverted.delete():
        palindromo = False
        break

if palindromo:
    print ("Es palindromo")
else:
    print ("No es palindromo")