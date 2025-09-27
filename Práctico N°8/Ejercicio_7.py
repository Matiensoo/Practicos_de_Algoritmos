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


file_name_1 = "texto ingresado.txt"

file_name_2 = "texto invertido.txt"

file_1 = open(file_name_1, "w")

file_2 = open(file_name_2, "w")

word = ""

P = Pila()

stop = False

while stop == False:

    line = input("Ingrese una línea de texto, si quiere parar, ingrese - : ")
    if line != "-":
        file_1.write(f"{line}\n")
    else:
        stop = True

file1 = open(file_name_1,"r")

for char in file1.read():
    if char != " " and char != "\n":
        word += char
    else:
        P.push(word)
        word = ""

P.show()

for element in P.list:
    file_2.write(f"{element}\n")

file2 = open(file_name_2,"r")

print(file2.read())