class Vehiculo:
    def __init__ (self, marca, modelo, patente, color):

        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Patente: {self.patente}, Color: {self.color}"



vehiculos = []
marcas = []

n = int(input("¿Cuántos vehículos tiene la familia? "))


for i in range(n):
    print(f"\nVehículo {i+1}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    patente = input("Patente: ")
    color = input("Color: ")

    vehiculos_mencionados = Vehiculo(marca, modelo, patente, color)
    vehiculos.append(vehiculos_mencionados)
    marcas.append (vehiculos_mencionados.marca)


print("\nVehículos ingresados:\n")
for v in vehiculos:
    print(v.__str__())


my_dict = {}

for element in marcas:
    if element in my_dict:
        my_dict[element] += 1
    else:
        my_dict[element] = 1

print(my_dict)
