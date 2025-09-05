class Student:
    def __init__ (self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification

    def __str__ (self):
        return f"Nombre: {self.name} \nEdad: {self.age} \nCalificacion: {self.qualification}"
        
student_1_name = input("Ingrese el nombre del alumno: ")
student_1_qualification = int(input("Ingrese la calificacion del alumno: "))
student_1_age = int(input("Ingrese la edad del alumno: "))

student_1 = Student(student_1_name,student_1_age, student_1_qualification)

print (student_1)

if student_1.qualification >= 60:
    print("El alumno esta aprobado")
else:
    print ("El alumno esta desaprobado")