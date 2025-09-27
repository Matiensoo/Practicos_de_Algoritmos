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

W.show()

while not W.empty_list():
    l = W.delete()
    W_Inverted.push(l)

W_Inverted.show()

