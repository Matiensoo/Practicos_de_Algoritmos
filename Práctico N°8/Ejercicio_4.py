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
        
ida = Pila()
vuelta = Pila()

ida.add_back("Pueblo origen")
vuelta.add_back ("Pueblo origen")


N_Pueblos = int(input("Cuantos pueblos ha pasado por su camino?: "))

for i in range (N_Pueblos):
    Pueblos = input("Ingrese los pueblos recorridos: ") 
    ida.push(Pueblos)
    vuelta.add_back(Pueblos)

ida.push("Pueblo destino")
vuelta.add_back ("Pueblo destino")

print (f"Camino de ida:")
ida.show()
print (f"Camino de vuelta: ")
vuelta.show()