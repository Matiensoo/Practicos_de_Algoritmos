import math
class Triangle :
    def __init__ (self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    def perimetro (self):
        
        return self.l1 + self.l2 + self.l3
    
    def area (self):
        s = (self.l1 + self.l2 + self.l3)/2
        return math.sqrt(s * (s - self.l1)*(s - self.l2) * (s - self.l3))
    
    def forma (self):
        if self.l1 == self.l2 == self.l3:
            return "Es un triangulo equilatero" 
        elif self.l1 == self.l2 or self.l2 == self.l3 or self.l1 == self.l3:
            return "Es un triangulo isosceles"
        else:
            return "Es un triangulo escaleno"
    
triangulo_1 = Triangle (10, 9, 5)

triangulo_2 = Triangle (20, 18, 10)

print (f"Caracteristicas del triangulo 1: \n Perimetro: {triangulo_1.perimetro()} \n Area: {triangulo_1.area()} \n Forma: {triangulo_1.forma()}")

print (f"\nCaracteristicas del triangulo 2: \n Perimetro: {triangulo_2.perimetro()} \n Area: {triangulo_2.area()} \n Forma: {triangulo_2.forma()}")

