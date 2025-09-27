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

patient_queue = Cola()
obra_social_list = []

patient = ""
obra_social = ""
patient_counter = 0
obra_social_counter = 0

while patient != "-":
    patient = input("Ingrese el nombre del paciente, para parar ingrese - : ")
   
    if patient != "-":
        patient_counter += 1
        patient_queue.queue(patient)
        obra_social = input("Ingrese la obra social del paciente, en caso de no tener ingrese - : ")

        if obra_social != "-":
            obra_social_list.append(obra_social)
        else: obra_social_list.append("No tiene")

for i in obra_social_list:
    if i == "No tiene":
        obra_social_counter += 1

print("Usted tiene los siguientes paciente: ")
patient_queue.show()
print(f"De estos, hay {obra_social_counter} sin obra social y {patient_counter-obra_social_counter} que tienen obra social.")
