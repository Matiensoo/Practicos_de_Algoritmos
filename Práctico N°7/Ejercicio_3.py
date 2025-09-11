class Persona:
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}"

    def Mayor_de_edad(self):
        return self.edad >= 18



persona_1 = Persona("Juan", "Paco", 20, "40222111")

print(f"Características de la Persona 1: \n{persona_1.__str__()}")

if persona_1.Mayor_de_edad:
    print ("Es mayor de edad?: Si")
else:
    print("Es mayor de edad?: No")

persona_2 = Persona("Pepe", "Martinez", 15, "50333444")

print(f"\nCaracterísticas de la Persona 2: \n{persona_2.__str__()}")

if persona_2.Mayor_de_edad:
    print ("Es mayor de edad?: Si")
else:
    print("Es mayor de edad?: No")
