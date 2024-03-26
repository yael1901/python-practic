import math 



class triangulo:

    def __init__(self, altura, base):
        
        self.altura = altura
        self.base = base

    def area(self):

        area = (self.altura * self.base)/2
        print(area)
    
    def perimetro(self):
        
        perimetro = ((self.altura**2)+(self.base**2))
        print(math.sqrt(perimetro))

uno = triangulo(5,2)
uno.area()
uno.perimetro()
