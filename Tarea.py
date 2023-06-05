import math

from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, altura:float=0.0, base:float=0.0 ):
        super()._init_(alto=altura, ancho=base )


    def __str__(self):
        return f'Triangulo [altura ={self.alto}, base = {self.ancho}, ]'

    def calcular_area(self):
        return (self.ancho * self.alto)/2

    def calcular_perimetro(self):
        return 3 * self.ancho

if _name_ == '_main_':
    c1 = Triangulo(base=6, altura=18)
    print(c1)
    print(f'El área del Triangulo es: {c1.calcular_area()}')
    print(f'El perimetro del Triangulo es: {c1.calcular_perimetro()}')