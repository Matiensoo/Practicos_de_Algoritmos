class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):

        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calculo_salario(self):
        return self.horas_trabajadas * self.tarifa_hora

    def __str__(self):
        return f"Empleado: {self.nombre} \nHoras: {self.horas_trabajadas} \nTarifa: {self.tarifa_hora}"


empleados = []


n = int(input("¿Cuántos empleados desea cargar? "))


for i in range(n):
    print(f"\nEmpleado {i+1}:")
    nombre = input("Nombre: ")
    horas = int(input("Horas trabajadas: "))
    tarifa = float(input("Tarifa por hora: "))
    empleados.append(Empleado(nombre, horas, tarifa))


print("\nSueldos Correspondientes:")
for empleado in empleados:
    print(f"Sueldo de {empleado.nombre}: {empleado.calculo_salario()}")
