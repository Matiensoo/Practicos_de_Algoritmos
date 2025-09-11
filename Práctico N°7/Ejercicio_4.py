class Planeta:
    
    def __init__ (self, nombre="", satelite=0, masa=0, volumen=0, diametro=0, distancia_al_sol=0, tipo="", observable=False ):

        self.nombre = nombre
        self.satelite = satelite
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_al_sol = distancia_al_sol
        self.tipo = tipo
        self.observable = observable
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nSatélite: {self.satelite} \nMasa: {self.masa} \nVolumen: {self.volumen} \nDiámetro: {self.diametro} \nDistáncia al sol: {self.distancia_al_sol} \nTipo: {self.tipo} \nObservable: {self.observable}"
    
    def densidad(self):
        return self.masa / self.volumen
    
    def exterior(self):
        if (self.distancia_al_sol / 149597870) > 3.4:
            return "El planeta se considera exterior al sistema solar"
        else:
            return "El planeta esta dentro del sistema solar"

planeta_1 = Planeta("Tierra", 1, 5.97e24, 1.08321e12, 12742, 149597870, "Terrestre", True)

print (f"Características del planeta 1: \n{planeta_1.__str__()} \nDensidad: {planeta_1.densidad()} \n{planeta_1.exterior()}")

planeta_2 = Planeta("Kepler-296 d", 79, 1.898e27, 1.4313e15, 139820, 1092301928401928021203, "Gaseoso", True)

print (f"\nCaracterísticas del planeta 2: \n{planeta_2.__str__()} \nDensidad: {planeta_2.densidad()} \n{planeta_2.exterior()}")