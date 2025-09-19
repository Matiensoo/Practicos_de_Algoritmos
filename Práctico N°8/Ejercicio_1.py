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
    
    def show (self):
       print (self.list)
        
Pila_1 = Pila()
Pila_2 = Pila()

for i in range (3):
    element = int(input("Ingrese los numeros que desee: "))
    Pila_1.push(element)
    Pila_2.add_back(element)

Pila_1.show()
Pila_2.show()