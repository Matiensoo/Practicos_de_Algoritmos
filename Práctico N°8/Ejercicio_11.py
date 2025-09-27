class Cola:
    def __init__ (self):
        self.list = []

    def queue (self, name, sheets):
        self.list.append({"Nombre" : name, "Hojas" : sheets})
        return self.list

    def dequeue (self):
        self.list.pop(0)
    
    def empty_list(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def show (self):
        print (self.list)

printer = Cola()
option = None

while option != 0:
    option = int(input("Ingrese 1 si quiere ingresar un archivo. Ingrese 2 si desea imprimir el primer archivo. Ingrese 0 si desea terminarla impresión: "))
    if option == 1:    
        name = input("Ingrese el nombre del archivo: ")
        sheets = input("Ingrese la cantidad de hojas del archivo: ")
        printer.queue(name, sheets)
    elif option == 2:
        print(f"Imprimiendo {printer.list[0] ['Nombre']}")
        printer.dequeue()
    elif option == 0:
        print("Impresión terminada. Adios :)")
    else:
        print("Opción no valida, intentelo otra vez")
        pass