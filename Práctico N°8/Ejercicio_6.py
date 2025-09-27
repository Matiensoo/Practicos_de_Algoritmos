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

containers = Pila()
new_containers = Pila()
selected_container = Pila()

amount = int(input("Ingrese el numero de contenedores que tenga: "))

i = 1

while i <= amount:
    containers.push(f"Contenedor n° {i} ") 
    i += 1

containers.show()

extract = 0

extract = int(input("Ingrese qué contenedor quiere retirar: ")) + 1

difference = amount - extract + 1

i = 0

if extract <= amount:
    while i < amount:
        new_containers.list.append(containers.list[0])
        containers.pop()
        i += 1
        if i == difference:
            selected_container.push(containers.list[0])
            containers.pop()
            i += 1

new_containers.show()
selected_container.show()