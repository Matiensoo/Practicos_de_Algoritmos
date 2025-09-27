class Cola:
    def __init__ (self):
        self.list = []

    def queue (self, elements):
        self.list.append(elements)

    def dequeue (self):
        self.list.pop(0)
    
    def empty_list(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def show (self):
        print (self.list)

person_queue = Cola()

mail_continue = True

continue_queue = "si"

i = 0

while mail_continue == True:
    while i < 5:
        person_queue.queue(input("Ingrese el nombre de la carta a entregar.\nRecuerde que no se aceptarán más de 5 cartas por persona: "))
        i += 1
        if i == 5:
            print("Usted ha alcanzado el limite de cartas permitido, si desea entregar mas, haga la fila otra vez")
    i = 0

    continue_queue = input("Si desea hacer la cola otra vez, ingrese si. En caso contrario, ingrese no: ")
    if continue_queue == "si":
         mail_continue = True
    elif continue_queue == "no":
         mail_continue = False

person_queue.show()