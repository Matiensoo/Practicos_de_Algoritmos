class Pila:
    def __init__ (self):
        self.list = []
        
    def push (self, elements):
        self.list.append(elements)

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


P = Pila()

chain = input("Ingrese su cadena de texto: ")

balanced = True

for element in chain:
    if element == "(":
        P.push(element)
    if element == ")":
        if P.empty_list():
            balanced = False
            break
        else:
            P.pop()

if P.empty_list() and balanced == True:
    print("Balanceado")
    
else:
    print("No Balanceado")